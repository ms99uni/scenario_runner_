from srunner.tools import dotdict
from agent import Trainer, Decay_Explore_Rate
from model import hd_net_args, HDDriveDQN

scenario_args = dotdict()
scenario_args.host = '127.0.0.1'
scenario_args.port = '2000'
scenario_args.timeout = '10.0'
scenario_args.trafficManagerPort = '8000'
scenario_args.trafficManagerSeed = '0'
scenario_args.sync = True # is required when training
scenario_args.list = False
scenario_args.scenario = 'StraightDriving_1'
scenario_args.openscenario = None 
scenario_args.openscenarioparams = None 
scenario_args.route = None
# scenario_args.agent = '.\\srunner\\autoagents\\human_agent.py' # agent module location
scenario_args.agent = '.\\srunner\\autoagents\\npc_agent.py' # agent module location
# scenario_args.agent = '.\\srunner\\autoagents\\simple_agent.py' # agent module location
scenario_args.agentConfig = '.\\srunner\\autoagents\\simple_agent_config.txt' 
scenario_args.output = False
scenario_args.file = False 
scenario_args.junit = False 
scenario_args.json = False 
scenario_args.outputDir = '' 
scenario_args.configFile = ''
scenario_args.additionalScenario = '' 
scenario_args.debug = False 
scenario_args.reloadWorld = True 
scenario_args.record = '' 
scenario_args.randomize = False 
scenario_args.repetitions = 1
scenario_args.waitForEgo = False
scenario_args.is_learner = True  
scenario_args.useMPI = True
scenario_args.drawWaypoints = True
scenario_args.route_dist = 200
scenario_args.raise_excep = False

agent_config = dotdict({
            'sensor_setup': 'hd_map',
            'image_width': '96',
            'image_height': '96',
            'visualize_sensors': '1',
            'external_visualizer': '1',
            'fill_buffer': '0',
            'file': 'test.json',
        })

exp_args = dotdict()
exp_args.BATCH_SZ = 32 # batch size for replay training
exp_args.REPLARY_MEM_SZ = 15_000 # size of the buffer to store (s,a,r,s') tuples
exp_args.NUM_FRAMES = 4  # number of temporal frames the model should use
exp_args.START_STEP = 0 # to restart from previous crash point
exp_args.NUM_STEPS = 200_000 # number of steps/frames to train on
exp_args.MODEL_NAME = 'hd_1'
exp_args.LOAD_MODEL = True
exp_args.TEST = False

model = HDDriveDQN
model_args = hd_net_args
explore_rate = Decay_Explore_Rate


if __name__ == '__main__':
    try:
        print("Starting training of agent")
        trainer = Trainer(scenario_args, agent_config, model, 
                          model_args, exp_args, explore_rate, debug=False)
        trainer.train()
        scenario_args = trainer.scenario_specifications        
    finally:
        print("Disconnecting")
        trainer.env.comm.Disconnect() 