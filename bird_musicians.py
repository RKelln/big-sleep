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

output_path = 'output/test8/'
seed = 500

for i in range(3):
    seed += 1
    dream = Imagine(
        text = "An ostrich playing an upright bass | bird playing music | artstation",
        output_path = output_path + 'caleb',
        seed = seed,
        **defaults
    )
    dream()


    seed += 1
    dream = Imagine(
        text = "An owl playing a piano | bird playing a piano | artstation",
        output_path = output_path + 'chris',
        seed = seed,
        **defaults
    )
    dream()


    seed += 1
    dream = Imagine(
        text = "A heron playing the drums | bird playing drums | artstation",
        output_path = output_path + 'sarah',
        seed = seed,
        **defaults
    )
    dream()

    seed += 1
    dream = Imagine(
        text = "Three birds playing bass, piano and drums | birds playing music | artstation",
        output_path = output_path + 'trio',
        seed = seed,
        **defaults
    )
    dream()


    seed += 1
    dream = Imagine(
        text = "A robin using a computer to edit video | bird using a computer | artstation",
        output_path = output_path + 'ryan',
        seed = seed,
        **defaults
    )
    dream()


    seed += 1
    dream = Imagine(
        text = "A bluejay writing music on paper | bird writing music | artstation",
        output_path = output_path + 'jackson',
        seed = seed,
        **defaults
    )
    dream()


    # seed += 1
    # dream = Imagine(
    #     text = "Birds of a feather, flock together | flock of colorful birds | artstation",
    #     output_path = output_path + 'birds_of_a_feather',
    #     seed = seed,
    #     **defaults
    # )
    # dream()


