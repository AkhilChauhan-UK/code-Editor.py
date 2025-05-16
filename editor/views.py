import subprocess
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

def index(request):
    return render(request, 'editor/index.html')  # your editor page

@csrf_exempt
@require_POST
def run_code(request):
    code = request.POST.get('code', '')
    try:
        process = subprocess.run(
            ['python3', '-c', code],
            capture_output=True,
            text=True,
            timeout=5
        )
        output = process.stdout + process.stderr
    except subprocess.TimeoutExpired:
        output = 'Execution timed out.'

    return JsonResponse({'output': output})
