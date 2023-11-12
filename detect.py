from ultralytics import YOLO
from common import imwrite

def load_yolo_model(model_path='yolov8n.pt'):
    """_summary_

    Args:
        modelpath (str, optional): _description_. Defaults to 'yolov8n.pt'.
    """
    return YOLO(model_path)

def save_results_to_image(results, filename='output.jpg'):
    """
    Save the plotted results to an image file.

    Parameters:
    - results: A list containing result objects with a plot method.
    - filename: The name of the image file to save the results. Default is 'result.jpg'.
    """
    for r in results:
        im_array = r.plot()
        imwrite(filename, im_array)
        