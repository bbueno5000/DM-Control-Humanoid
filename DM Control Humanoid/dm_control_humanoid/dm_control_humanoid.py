from dm_control import suite
from dm_control import viewer
import numpy as np

env = suite.load(domain_name="humanoid", task_name="stand")
action_spec = env.action_spec()

def random_policy(time_step):
    """
    Define a uniform random policy.
    """
    del time_step
    return np.random.uniform(
        low=action_spec.minimum,
        high=action_spec.maximum,
        size=action_spec.shape)

viewer.launch(env, policy=random_policy)

