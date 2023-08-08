from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def hello(request):
    return HttpResponse('''
        <h1>Hello from other side </h1>
    ''')

@csrf_exempt #stopping csrf security check
def addxy(request):
    if request.method == 'POST':
        x = request.POST.get('num1')
        y = request.POST.get('num2')

        z = int(x)+int(y)
        return HttpResponse("Result: " +str(z))
    else:
        return HttpResponse('''
        <!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Number Input Form</title>
<style>
  body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }

  .container {
    background-color: #fff;
    border-radius: 5px;
    padding: 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }

  .input-group {
    display: flex;
    flex-direction: column;
    margin-bottom: 15px;
  }

  label {
    font-weight: bold;
    margin-bottom: 5px;
  }

  input[type="number"] {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 3px;
  }

  button {
    background-color: #007BFF;
    color: #fff;
    border: none;
    padding: 10px 20px;
    border-radius: 3px;
    cursor: pointer;
    transition: background-color 0.3s ease;
  }

  button:hover {
    background-color: #0056b3;
  }
</style>
</head>
<body>
  <div class="container">
    <form action="#" method="post">
      <div class="input-group">
        <label for="num1">Number 1</label>
        <input type="number" id="num1" name="num1" required>
      </div>
      <div class="input-group">
        <label for="num2">Number 2</label>
        <input type="number" id="num2" name="num2" required>
      </div>
      <button type="submit">Submit</button>
    </form>
  </div>
</body>
</html>

    ''')
    # else:
    #     return HttpResponse('''
    #     HEllo
    # ''')