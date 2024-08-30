from django.shortcuts import render,redirect,HttpResponse
from Home.models import Quiz
import random

# Create your views here.
def home(request):
    
    quizs = Quiz.objects.filter(status = False)
    quiz_list = list(quizs)
    
    if not quiz_list:
        print("No quizzes available.")
        return redirect('end')
    
    
    quiz = random.choice(quiz_list)
    request.session['quiz_number'] = quiz.number
    
    context = {
        "quiz":quiz
    }
    
    if 'attempted' not in request.session:
        request.session['attempted'] = 0
    if 'correct' not in request.session:
        request.session['correct'] = 0
    if 'attempted_quizzes' not in request.session:
        request.session['attempted_quizzes'] = []
        
    return render (request, 'quiz.html',context)

def submit_answer(request):
    
    if request.method == 'POST':
        selected_option = request.POST.get('option')
        quiz_number = request.session.get('quiz_number')
        attempted = request.session.get('attempted', 0)
        correct = request.session.get('correct', 0)
        attempted_quizzes = request.session.get('attempted_quizzes', [])
        selected_options = request.session.get('selected_options', {})
        
        try:
            quiz = Quiz.objects.get(number=quiz_number)
        except Quiz.DoesNotExist:
            return redirect('home')
        
        
        quiz.status = True
        quiz.save()
        
        
        is_correct = selected_option == quiz.answer
        if is_correct:
            correct += 1
        attempted += 1
        
        request.session['attempted'] = attempted
        request.session['correct'] = correct
            
        if quiz_number not in attempted_quizzes:
            attempted_quizzes.append(quiz_number)
        request.session['attempted_quizzes'] = attempted_quizzes
        
        selected_options[quiz_number] = selected_option
        request.session['selected_options'] = selected_options
        
        result_message = f"CORRECT" if is_correct else f"WRONG"
        
        context = {
            'result_message': result_message,
            'quiz': quiz,
            'selected_option': selected_option,
            'is_correct': is_correct,
            'attempted':attempted,
            'correct':correct,
        }
         
        return render (request, 'result.html', context)
    return redirect('home')

def end(request):
    attempted = request.session.get('attempted', 0)
    correct = request.session.get('correct', 0)
    attempted_quizzes = request.session.get('attempted_quizzes', [])
    selected_options = request.session.get('selected_options', {})
    
    print("Selected Options in Session:", selected_options)  # Print or log to check contents


    # Fetch all attempted quizzes from the database
    quizzes = Quiz.objects.filter(number__in=attempted_quizzes)

    # Prepare a list to hold quiz and selected option pairs
    quizzes_with_options = []
    for quiz in quizzes:
        option = selected_options.get(str(quiz.number), "Not attempted")
        quizzes_with_options.append({
            'quiz': quiz,
            'selected_option': option,
        })
    print (quizzes_with_options)

    result_message = {
        'attempted': attempted,
        'correct': correct,
        'quizzes_with_options': quizzes_with_options
    }

    return render(request, 'final.html', result_message)

def restart_quiz(request):
    Quiz.objects.update(status=False)
    request.session.pop('attempted', None)
    request.session.pop('correct', None)
    request.session.pop('quiz_number', None)
    request.session.pop('attempted_quizzes', None)
    request.session.pop('selected_options', None)
    return redirect('home')