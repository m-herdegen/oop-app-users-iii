from users.User import User
from users.FreeUser import FreeUser 
from users.PremiumUser import PremiumUser 

talulah = FreeUser('talulah', 'talulah@email.com', 'aksjhdfoa;wehflksd')
beau = FreeUser('beau', 'beau@email.com', 'aksjhdfoa;wehflksd')
emmett = PremiumUser('emmett', 'emmett@email.com', 'aksjhdfoa;wehflksd')
victor = PremiumUser('victor', 'victor@email.com', 'aksjhdfoa;wehflksd')


talulah.add_post('1')
talulah.add_post('2')
talulah.add_post('3')

victor.add_post('1')
victor.add_post('2')
victor.add_post('3')
victor.add_post('4')

print(talulah, '\n', beau, '\n', emmett, '\n', victor)

print(User.post_hist)