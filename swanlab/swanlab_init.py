import swanlab

swanlab.login(api_key="", save=True)
run = swanlab.init(
    # set project name
    project="my-project",
    # hyper parameter, no real meaning
    config={
        "learning_rate": 0.01,
        "epochs": 10,
    },
)

loss = 0.1
run.log({"loss":loss}) # it will sent a statistic to server