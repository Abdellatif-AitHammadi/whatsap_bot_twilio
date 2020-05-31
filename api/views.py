from core import *
class Service(threading.Thread):
    def __init__(self, incoming_message):
        threading.Thread.__init__(self)
        self.incoming_message = incoming_message
    def run(self):
        incoming_message = self.incoming_message
@csrf_exempt
def namayto(request):
    response = MessagingResponse()
    name = request.POST.get('Body', '')
    z = str(name)
    print(z)
    if z=="":
        pass
    elif z[0] == "?":
        response.message(wikipedia.summary(z[1:]))
    elif z[0] == ".":
        response.message(trad(z[1:], "ar"))
    elif z[0] == "*":
        response.message(trad(z[1:], "fr"))
    elif z[0] == "+":
        response.message(trad(z[1:], "en"))
    elif z[0] == "=":
        if z == "=":
            data = json.loads(open("motamadris/0.json").read())
            s=""
            for d in data:
                s+=" =%s " % (d["id"])
                s+="%s" % (d["title"])
            response.message(s)
        try:
            data = json.loads(open("motamadris/%s.json" % (z[1:])).read())
            s=""
            for d in data:
                s+=" =%s_%s " % (z[1:], d["id"])
                s+=" %s" % (d["title"])
            response.message(s)
        except:
            pass
        try:
            A = z[1:].split("_")
            d = A[-1]
            A = "_".join(A[:-1])
            data = json.loads(open("motamadris/P%s.json" % (A)).read())
            msg = response.message(data[int(d) - 1]["title"])
            href = data[int(d) - 1]["href"]
            if "pdf" in href:
                msg.media(href)
        except:
            pass
    else:
        data = json.loads(open("motamadris/0.json").read())
        s=""
        for d in data:
            s+=" =%s " % (d["id"])
            s+="%s" % (d["title"])
        response.message(s)
        # msg=response.message('Namayto')
        # GOOD_BOY_URL = "https://images.unsplash.com/photo-1518717758536-85ae29035b6d?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"
        # msg.media(GOOD_BOY_URL)
    return HttpResponse(response)
