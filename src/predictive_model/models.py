from enum import Enum

from django.db import models

from src.common.models import CommonModel


class PredictiveModels(Enum):
    CLASSIFICATION = 'classification'
    REGRESSION = 'regression'
    TIME_SERIES_PREDICTION = 'timeSeriesPrediction'


PREDICTIVE_MODEL_MAPPINGS = (
    (PredictiveModels.CLASSIFICATION.value, 'classification'),
    (PredictiveModels.REGRESSION.value, 'regression'),
    (PredictiveModels.TIME_SERIES_PREDICTION.value, 'timeSeriesPrediction')
)


class PredictiveModel(CommonModel):
    """Container of Classification to be shown in frontend"""
    model_path = models.FilePathField(path='cache/model_cache/')
    predictive_model = models.CharField(choices=PREDICTIVE_MODEL_MAPPINGS, max_length=20)
    prediction_method = models.CharField(max_length=20)

    @staticmethod
    def init(configuration: dict):
        prediction_type = configuration['predictive_model']
        if prediction_type == PredictiveModels.CLASSIFICATION.value:
            from src.predictive_model.classification.models import Classification
            return Classification.init(configuration)
        elif prediction_type == PredictiveModels.REGRESSION.value:
            from src.predictive_model.regression.models import Regression
            return Regression.init(configuration)
        elif prediction_type == PredictiveModels.TIME_SERIES_PREDICTION.value:
            from src.predictive_model.time_series_prediction.models import TimeSeriesPrediction
            return TimeSeriesPrediction.init(configuration)
        else:
            raise ValueError('predictive model type {} not recognized'.format(prediction_type))

    def to_dict(self):
        return {
            'model_path': self.model_path,
            'predictive_model': self.predictive_model,
            'prediction_method': self.prediction_method
        }
