from big_sleep import Imagine


defaults = dict(
    lr = .09,
    save_every = 0,
    save_progress = True,
    save_best = True,
    image_size = 512,
    epochs = 23,
    iterations = 200,
    append_seed = True,
)

output_path = 'output/test7/'
seed = 1000

# The reason birds can fly and we can't is simply because they have perfect faith, for to have faith is to have wings.
# Faith is the bird that feels the light when the dawn is still dark.
# There are joys which long to be ours. God sends 10,000 truths, which come about us like birds seeking inlet; but we are shut up to them, and so they bring us nothing, but sit and sing awhile upon the roof, and then fly away.
# Those little nimble musicians of the air, that warble forth their curious ditties, with which nature hath furnished them to the shame of art.
# Happier of happy though I be, like them I cannot take possession of the sky, mount with a thoughtless impulse, and wheel there, one of a mighty multitude whose way and motion is a harmony and dance magnificent.
# In order to see birds it is necessary to become part of the silence.
# I know why the caged bird sings, ah me, when his wing is bruised and his bosom sore; when he beats his bars and he would be free, it is not a carol of joy or glee, but a prayer that he sends from his heart's deep core.
# The bird of paradise alights only upon the hand that does not grasp.
# The soul that is attached to anything however much good there may be in it, will not arrive at the liberty of divine union. For whether it be a strong wire rope or a slender and delicate thread that holds the bird, it matters not, if it really holds it fast; for, until the cord be broken the bird cannot fly.
# Birds sing after a storm; why shouldn't people feel as free to delight in whatever sunlight remains to them?
# Have you ever observed a humming-bird moving about in an aerial dance among the flowers, a living prismatic gem, it is a creature of such fairy-like loveliness as to mock all description.
# Use what talents you possess: the woods would be very silent if no birds sang there except those that sang best.
# The very idea of a bird is a symbol and a suggestion to the poet. A bird seems to be at the top of the scale, so vehement and intense his life ... The beautiful vagabonds, endowed with every grace, masters of all climes, and knowing no bounds—how many human aspirations are realized in their free, holiday-lives—and how many suggestions to the poet in their flight and song!
# Hold fast to dreams, for if dreams die, life is a broken-winged bird that cannot fly.
# Did you ever see an unhappy horse? Did you ever see bird that had the blues? One reason why birds and horses are not unhappy is because they are not trying to impress other birds and horses.
# Intelligence without ambition is a bird without wings.
# Sweet the coming on/Of grateful evening mild; then silent night/With this her solemn bird and this fair moon,/And these the gems of heaven, her starry train.
# Be as a bird perched on a frail branch that she feels bending beneath her, still she sings away all the same, knowing she has wings
# I would rather learn from one bird how to sing than to teach 10,000 stars how not to dance.
# The greatest achievement was at first and for a time a dream. The oak sleeps in the acorn, the bird waits in the egg, and in the highest vision of the soul a waking angel stirs. Dreams are the seedlings of realities.
# The birds are moulting. If only man could moult also — his mind once a year its errors, his heart once a year its useless passions.
# It is not only fine feathers that make fine birds.
# You have to believe in happiness, or happiness never comes. Ah, that's the reason a bird can sing. On his darkest day he believes in spring.
# Love is a bird; she needs to fly.
# Hail to thee, blithe spirit! Bird thou never wert That from Heaven, or near it, Pourest thy full heart In profuse strains of unpremeditated art.
# No bird soars too high, if he soars with his own wings
# Why do birds sing in the morning? It's the triumphant shout: We got through another night
# Each bird must sing with his own throat
# Even when a bird walks, one feels it has wings

for i in range(4):
    seed += 1
    dream = Imagine(
        text = "The reason birds can fly and we can't is simply because they have perfect faith, for to have faith is to have wings | artstation",
        output_path = output_path + 'reason_birds_can_fly',
        seed = seed,
        **defaults
    )
    dream()


    seed += 1
    dream = Imagine(
        text = "Faith is the bird that feels the light when the dawn is still dark | artstation",
        output_path = output_path + 'faith_is_the_bird',
        seed = seed,
        **defaults
    )
    dream()


    seed += 1
    dream = Imagine(
        text = "In order to see birds it is necessary to become part of the silence | artstation",
        output_path = output_path + 'become_the_silence',
        seed = seed,
        **defaults
    )
    dream()


    seed += 1
    dream = Imagine(
        text = "Hold fast to dreams, for if dreams die, life is a broken-winged bird that cannot fly | artstation",
        output_path = output_path + 'hold_fast_to_dreams',
        seed = seed,
        **defaults
    )
    dream()


    seed += 1
    dream = Imagine(
        text = "I would rather learn from one bird how to sing than to teach 10,000 stars how not to dance | artstation",
        output_path = output_path + 'learn_from_one_bird',
        seed = seed,
        **defaults
    )
    dream()


    seed += 1
    dream = Imagine(
        text = "Each bird must sing with his own throat | artstation",
        output_path = output_path + 'sing_wth_own_throat',
        seed = seed,
        **defaults
    )
    dream()





