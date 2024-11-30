# Define the directories
DATA_DIR = data
MODELS_DIR = models
SCRIPTS_DIR = scripts

# Define the Python scripts
DATA_PREP_SCRIPT = $(SCRIPTS_DIR)/data_prep.py
TRAIN_SCRIPT = $(SCRIPTS_DIR)/train_model.py
EVALUATE_SCRIPT = $(SCRIPTS_DIR)/evaluate_model.py
DEPLOY_SCRIPT = $(SCRIPTS_DIR)/deploy_model.py

# Define the targets
.PHONY: data
data: $(DATA_PREP_SCRIPT)
	@echo "Installing dataset..."
	python $(DATA_PREP_SCRIPT)
	

.PHONY: train
train: $(DATA_PREP_SCRIPT) $(TRAIN_SCRIPT)
	@echo "Training the model..."
	python $(TRAIN_SCRIPT)

.PHONY: evaluate
evaluate: $(TRAIN_SCRIPT) $(EVALUATE_SCRIPT)
	@echo "Evaluating the model..."
	python $(EVALUATE_SCRIPT)

.PHONY: deploy
deploy: $(TRAIN_SCRIPT) $(DEPLOY_SCRIPT)
	@echo "Deploying the model..."
	python $(DEPLOY_SCRIPT)


# Virtual Environemnt
VENV_DIR = myenv

.PHONY: venv 
venv:
	@echo "Creating virtual environment..."
	python -m venv $(VENV_DIR)
	@echo "To activate your virtual environment, enter this command '$(VENV_DIR)\Scripts\activate'"

.PHONY: install
install: 
	@echo "Installing requirements..."
	pip install -r requirements.txt
