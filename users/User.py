class User:

    post_hist = {}
    def __init__(self,name,email_address,license_num):
        self.name = name
        self.email_address = email_address
        self.license_num = license_num
    
    def __str__(self):
        return f"{self.name} has email {self.email_address} and license # {self.license_num}."

    @property
    def post(self):
        return User.post_hist

    @post.setter
    def add_post(self, message):
        if self.name not in User.post_hist.keys():
            User.post_hist[self.name] = [message]
        else:
            User.post_hist[self.name].append(message)

    def remove_post(self, post_text):
        for i,item in enumerate(User.post_hist[self.name]):
            if post_text == item:
                User.post_hist[self.name].pop(i)