from users.User import User 

class FreeUser(User):

    def add_post(self, message):
        if self.name not in User.post_hist.keys():
            User.post_hist[self.name] = [message]
        elif len(User.post_hist[self.name]) < 2:
            User.post_hist[self.name].append(message)