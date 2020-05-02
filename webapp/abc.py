from django.http import HttpResponse
from django.shortcuts import render



def home(request):
    return render(request,"index.html",{'key1': 'I am coming from home page'})		


def result(request):


	age = request.GET['age']	
	name = request.GET['name']
	comment = request.GET['comment']
	word = len(comment.split(' '))
	words = comment.split(' ')
	counts = {}
	for i in words:
		if i in counts:
			counts[i] += 1
		else:
			counts[i] = 1

		

	
	a = {'age': age,
		 'name':name,
		 'comment': comment,
		 'word': word,
		 'counts':counts	}
		 



	return render(request,"result.html", {'a':a})	


