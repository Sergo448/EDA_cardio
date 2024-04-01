import config as config
import process.preprocess as prepr
import process.visualization as vis

data = prepr.get_data(path=config.DATA_PATH, debug=config.DEBUG)

""" collecting info """
prepr.get_info_and_save_to_txt(data=data,
                               result_path=os.path.join(config.RESULT_PATH),
                               debug=config.DEBUG)

prepr.describe_and_save_to_json(data=data,
                                result_path=os.path.join(config.RESULT_PATH),
                                debug=config.DEBUG)

prepr.count_null_values(data = data, result_path = os.path.join(config.RESULT_PATH))

prepr.print_values_in_df(data = data, result_path = os.path.join(config.RESULT_PATH))

""" collecting plots """
vis.height_hist_bins_20(data = data, result_path=config.RESULT_PATH)
vis.lsdweight_hist_bins_20(data = data, result_path=config.RESULT_PATH)