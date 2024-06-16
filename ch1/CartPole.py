import gym  # 导入 Gym 的 Python 接口环境包
env = gym.make('CartPole-v1')  # 构建实验环境
env.new_step_api = True
env.reset()  # 重置一个回合
for i in range(20):
    print("The %d times: " % i)
    env.render()  # 显示图形界面
    action = env.action_space.sample() # 从动作空间中随机选取一个动作
    observation, reward, done, info, _ = env.step(action)
    print(observation)
env.close() # 关闭环境

from gym import envs
env_specs = envs.registry.values()
envs_ids = [env_spec.id for env_spec in env_specs]
print(envs_ids)
