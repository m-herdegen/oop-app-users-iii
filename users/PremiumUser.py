from users.User import User 

class PremiumUser(User):
    def add_post(self, message):
        if self.name not in User.post_hist.keys():
            User.post_hist[self.name] = [message]
        else:
            User.post_hist[self.name].append(message)
