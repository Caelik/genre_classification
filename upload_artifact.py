import wandb

# Initialize a W&B run in the 'exercise_14' project
run = wandb.init(project="exercise_14")

# Create an artifact of type 'dataset' and add the file
artifact = wandb.Artifact('data_train.csv', type='dataset')

# Specify the path to your 'data_train.csv' file
artifact.add_file('data_train.csv')

# Log the artifact to W&B
run.log_artifact(artifact)

# Finish the W&B run
run.finish()
