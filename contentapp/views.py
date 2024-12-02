from django.shortcuts import render
import re
import replicate
# Create your views here.


def index(request):

    if request.method == "POST":
        input_text = request.POST["entered_text"]
        client = replicate.Client(api_token="r8_7CaBd3kfiCvz6L4mdeIm7HULfbcwULU1tk2VA")
        output = client.run("meta/meta-llama-3.1-405b-instruct",input={"prompt":input_text,"max_token":500})
        final_response = "".join(output)
        cleaned_text = re.sub(r'\s+',' ',final_response).strip()
        
        context = {"cleaned_text":cleaned_text}
        return render(request,"index.html",context)
    
    else:
        return render(request,"index.html")





