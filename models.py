class User:
    name=None
    email=None
    def send_email(self):
        if self.email is not None:
            print("Sending email:"+ self.email)
        else: 
            print("Error")
    def __init__(self, name, email):
        self.name=name
        self.email=email
    def __str__(self):
        return"user:" + self.email

class student (User):
    id=None
    score=None

    def is_approvate(self):
            return self.score>=8

    def __init__(self,
        name=None, 
        email=None,
        id=None,
        score=None
    ):
        super().__init__(name,email)
        self.id=uuid.uuid4()
        self.score=score

    def __repr__(self):
            return f"student(name='{self.name}',email='{self.name}',id='{self.id}',score='{self.score}')"
        

    def __str__(self):
            return "student:"+str(self.id)+","+self.email
    
    
