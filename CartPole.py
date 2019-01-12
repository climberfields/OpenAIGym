import gym
from gym import spaces
space = spaces.Discrete(8)
x = space.sample()
assert space.contains(x)
assert space.n == 8
env = gym.make('CartPole-v0')
print(env.action_space)
print(env.observation_space)
for _ in range(1000):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+ 1))
            break


env.close()