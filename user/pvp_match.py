from environment.environment import RenderMode, CameraResolution
from environment.agent import run_real_time_match
from user.train_agent import UserInputAgent, ConstantAgent, ClockworkAgent, SB3Agent, RecurrentPPOAgent #add anymore custom Agents (from train_agent.py) here as needed
from user.my_agent import SubmittedAgent
from user.train_agent import BasedAgent, BasedAgent1, BasedAgent2, BasedAgent3

import pygame
pygame.init()

my_agent = BasedAgent2()
# my_agent = SubmittedAgent(file_path='checkpoints/experiment_12/rl_model_3262000_steps.zip')

#Input your file path here in SubmittedAgent if you are loading a model:
opponent = BasedAgent()

match_time = 99999

# Run a single real-time match
print(run_real_time_match(
    agent_1=my_agent,
    agent_2=opponent,
    max_timesteps=30 * 999990000,  # Match time in frames (adjust as needed)
    resolution=CameraResolution.LOW,
))