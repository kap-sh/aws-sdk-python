"""Generated from Smithy shape ``com.amazonaws.forecast#DescribePredictorResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn
    import aws_sdk_forecast.types.arn_list
    import aws_sdk_forecast.types.auto_ml_override_strategy
    import aws_sdk_forecast.types.boolean
    import aws_sdk_forecast.types.encryption_config
    import aws_sdk_forecast.types.evaluation_parameters
    import aws_sdk_forecast.types.featurization_config
    import aws_sdk_forecast.types.forecast_types
    import aws_sdk_forecast.types.hyper_parameter_tuning_job_config
    import aws_sdk_forecast.types.input_data_config
    import aws_sdk_forecast.types.integer
    import aws_sdk_forecast.types.long
    import aws_sdk_forecast.types.message
    import aws_sdk_forecast.types.name
    import aws_sdk_forecast.types.optimization_metric
    import aws_sdk_forecast.types.predictor_execution_details
    import aws_sdk_forecast.types.status
    import aws_sdk_forecast.types.timestamp
    import aws_sdk_forecast.types.training_parameters


class DescribePredictorResponse(TypedDict):
    predictor_arn: NotRequired["aws_sdk_forecast.types.name.Name"]
    """<p>The ARN of the predictor.</p>"""
    predictor_name: NotRequired["aws_sdk_forecast.types.name.Name"]
    """<p>The name of the predictor.</p>"""
    algorithm_arn: NotRequired["aws_sdk_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the algorithm used for model training.</p>"""
    auto_ml_algorithm_arns: NotRequired["aws_sdk_forecast.types.arn_list.ArnList"]
    """<p>When <code>PerformAutoML</code> is specified, the ARN of the chosen algorithm.</p>"""
    forecast_horizon: NotRequired["aws_sdk_forecast.types.integer.Integer"]
    """<p>The number of time-steps of the forecast. The forecast horizon is also called the prediction length.</p>"""
    forecast_types: NotRequired["aws_sdk_forecast.types.forecast_types.ForecastTypes"]
    """<p>The forecast types used during predictor training. Default value is <code>[\"0.1\",\"0.5\",\"0.9\"]</code> </p>"""
    perform_auto_ml: NotRequired["aws_sdk_forecast.types.boolean.Boolean"]
    """<p>Whether the predictor is set to perform AutoML.</p>"""
    auto_ml_override_strategy: NotRequired[
        "aws_sdk_forecast.types.auto_ml_override_strategy.AutoMLOverrideStrategy"
    ]
    """<note> <p> The <code>LatencyOptimized</code> AutoML override strategy is only available in private beta. Contact Amazon Web Services Support or your account manager to learn more about access privileges. </p> </note> <p>The AutoML strategy used to train the predictor. Unless <code>LatencyOptimized</code> is specified, the AutoML strategy optimizes predictor accuracy.</p> <p>This parameter is only valid for predictors trained using AutoML.</p>"""
    perform_hpo: NotRequired["aws_sdk_forecast.types.boolean.Boolean"]
    """<p>Whether the predictor is set to perform hyperparameter optimization (HPO).</p>"""
    training_parameters: NotRequired[
        "aws_sdk_forecast.types.training_parameters.TrainingParameters"
    ]
    """<p>The default training parameters or overrides selected during model training. When running AutoML or choosing HPO with CNN-QR or DeepAR+, the optimized values for the chosen hyperparameters are returned. For more information, see <a>aws-forecast-choosing-recipes</a>.</p>"""
    evaluation_parameters: NotRequired[
        "aws_sdk_forecast.types.evaluation_parameters.EvaluationParameters"
    ]
    """<p>Used to override the default evaluation parameters of the specified algorithm. Amazon Forecast evaluates a predictor by splitting a dataset into training data and testing data. The evaluation parameters define how to perform the split and the number of iterations.</p>"""
    hpo_config: NotRequired[
        "aws_sdk_forecast.types.hyper_parameter_tuning_job_config.HyperParameterTuningJobConfig"
    ]
    """<p>The hyperparameter override values for the algorithm.</p>"""
    input_data_config: NotRequired[
        "aws_sdk_forecast.types.input_data_config.InputDataConfig"
    ]
    """<p>Describes the dataset group that contains the data to use to train the predictor.</p>"""
    featurization_config: NotRequired[
        "aws_sdk_forecast.types.featurization_config.FeaturizationConfig"
    ]
    """<p>The featurization configuration.</p>"""
    encryption_config: NotRequired[
        "aws_sdk_forecast.types.encryption_config.EncryptionConfig"
    ]
    """<p>An Key Management Service (KMS) key and the Identity and Access Management (IAM) role that Amazon Forecast can assume to access the key.</p>"""
    predictor_execution_details: NotRequired[
        "aws_sdk_forecast.types.predictor_execution_details.PredictorExecutionDetails"
    ]
    """<p>Details on the the status and results of the backtests performed to evaluate the accuracy of the predictor. You specify the number of backtests to perform when you call the operation.</p>"""
    estimated_time_remaining_in_minutes: NotRequired["aws_sdk_forecast.types.long.Long"]
    """<p>The estimated time remaining in minutes for the predictor training job to complete.</p>"""
    is_auto_predictor: NotRequired["aws_sdk_forecast.types.boolean.Boolean"]
    """<p>Whether the predictor was created with <a>CreateAutoPredictor</a>.</p>"""
    dataset_import_job_arns: NotRequired["aws_sdk_forecast.types.arn_list.ArnList"]
    """<p>An array of the ARNs of the dataset import jobs used to import training data for the predictor.</p>"""
    status: NotRequired["aws_sdk_forecast.types.status.Status"]
    """<p>The status of the predictor. States include:</p> <ul> <li> <p> <code>ACTIVE</code> </p> </li> <li> <p> <code>CREATE_PENDING</code>, <code>CREATE_IN_PROGRESS</code>, <code>CREATE_FAILED</code> </p> </li> <li> <p> <code>DELETE_PENDING</code>, <code>DELETE_IN_PROGRESS</code>, <code>DELETE_FAILED</code> </p> </li> <li> <p> <code>CREATE_STOPPING</code>, <code>CREATE_STOPPED</code> </p> </li> </ul> <note> <p>The <code>Status</code> of the predictor must be <code>ACTIVE</code> before you can use the predictor to create a forecast.</p> </note>"""
    message: NotRequired["aws_sdk_forecast.types.message.Message"]
    """<p>If an error occurred, an informational message about the error.</p>"""
    creation_time: NotRequired["aws_sdk_forecast.types.timestamp.Timestamp"]
    """<p>When the model training task was created.</p>"""
    last_modification_time: NotRequired["aws_sdk_forecast.types.timestamp.Timestamp"]
    """<p>The last time the resource was modified. The timestamp depends on the status of the job:</p> <ul> <li> <p> <code>CREATE_PENDING</code> - The <code>CreationTime</code>.</p> </li> <li> <p> <code>CREATE_IN_PROGRESS</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPING</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPED</code> - When the job stopped.</p> </li> <li> <p> <code>ACTIVE</code> or <code>CREATE_FAILED</code> - When the job finished or failed.</p> </li> </ul>"""
    optimization_metric: NotRequired[
        "aws_sdk_forecast.types.optimization_metric.OptimizationMetric"
    ]
    """<p>The accuracy metric used to optimize the predictor.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePredictorResponse) -> dict:
    out: dict = {}
    if "predictor_arn" in value:
        out["PredictorArn"] = value["predictor_arn"]
    if "predictor_name" in value:
        out["PredictorName"] = value["predictor_name"]
    if "algorithm_arn" in value:
        out["AlgorithmArn"] = value["algorithm_arn"]
    if "auto_ml_algorithm_arns" in value:
        import aws_sdk_forecast.types.arn_list

        out["AutoMLAlgorithmArns"] = (
            aws_sdk_forecast.types.arn_list.serialize_aws_json_1_1(
                value["auto_ml_algorithm_arns"]
            )
        )
    if "forecast_horizon" in value:
        out["ForecastHorizon"] = value["forecast_horizon"]
    if "forecast_types" in value:
        import aws_sdk_forecast.types.forecast_types

        out["ForecastTypes"] = (
            aws_sdk_forecast.types.forecast_types.serialize_aws_json_1_1(
                value["forecast_types"]
            )
        )
    if "perform_auto_ml" in value:
        out["PerformAutoML"] = value["perform_auto_ml"]
    if "auto_ml_override_strategy" in value:
        import aws_sdk_forecast.types.auto_ml_override_strategy

        out["AutoMLOverrideStrategy"] = (
            aws_sdk_forecast.types.auto_ml_override_strategy.serialize_aws_json_1_1(
                value["auto_ml_override_strategy"]
            )
        )
    if "perform_hpo" in value:
        out["PerformHPO"] = value["perform_hpo"]
    if "training_parameters" in value:
        import aws_sdk_forecast.types.training_parameters

        out["TrainingParameters"] = (
            aws_sdk_forecast.types.training_parameters.serialize_aws_json_1_1(
                value["training_parameters"]
            )
        )
    if "evaluation_parameters" in value:
        import aws_sdk_forecast.types.evaluation_parameters

        out["EvaluationParameters"] = (
            aws_sdk_forecast.types.evaluation_parameters.serialize_aws_json_1_1(
                value["evaluation_parameters"]
            )
        )
    if "hpo_config" in value:
        import aws_sdk_forecast.types.hyper_parameter_tuning_job_config

        out["HPOConfig"] = (
            aws_sdk_forecast.types.hyper_parameter_tuning_job_config.serialize_aws_json_1_1(
                value["hpo_config"]
            )
        )
    if "input_data_config" in value:
        import aws_sdk_forecast.types.input_data_config

        out["InputDataConfig"] = (
            aws_sdk_forecast.types.input_data_config.serialize_aws_json_1_1(
                value["input_data_config"]
            )
        )
    if "featurization_config" in value:
        import aws_sdk_forecast.types.featurization_config

        out["FeaturizationConfig"] = (
            aws_sdk_forecast.types.featurization_config.serialize_aws_json_1_1(
                value["featurization_config"]
            )
        )
    if "encryption_config" in value:
        import aws_sdk_forecast.types.encryption_config

        out["EncryptionConfig"] = (
            aws_sdk_forecast.types.encryption_config.serialize_aws_json_1_1(
                value["encryption_config"]
            )
        )
    if "predictor_execution_details" in value:
        import aws_sdk_forecast.types.predictor_execution_details

        out["PredictorExecutionDetails"] = (
            aws_sdk_forecast.types.predictor_execution_details.serialize_aws_json_1_1(
                value["predictor_execution_details"]
            )
        )
    if "estimated_time_remaining_in_minutes" in value:
        out["EstimatedTimeRemainingInMinutes"] = value[
            "estimated_time_remaining_in_minutes"
        ]
    if "is_auto_predictor" in value:
        out["IsAutoPredictor"] = value["is_auto_predictor"]
    if "dataset_import_job_arns" in value:
        import aws_sdk_forecast.types.arn_list

        out["DatasetImportJobArns"] = (
            aws_sdk_forecast.types.arn_list.serialize_aws_json_1_1(
                value["dataset_import_job_arns"]
            )
        )
    if "status" in value:
        out["Status"] = value["status"]
    if "message" in value:
        out["Message"] = value["message"]
    if "creation_time" in value:
        import aws_sdk_forecast.types.timestamp

        out["CreationTime"] = aws_sdk_forecast.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modification_time" in value:
        import aws_sdk_forecast.types.timestamp

        out["LastModificationTime"] = (
            aws_sdk_forecast.types.timestamp.serialize_aws_json_1_1(
                value["last_modification_time"]
            )
        )
    if "optimization_metric" in value:
        import aws_sdk_forecast.types.optimization_metric

        out["OptimizationMetric"] = (
            aws_sdk_forecast.types.optimization_metric.serialize_aws_json_1_1(
                value["optimization_metric"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePredictorResponse:
    out: DescribePredictorResponse = {}  # type: ignore[typeddict-item]
    if "PredictorArn" in data:
        out["predictor_arn"] = data["PredictorArn"]
    if "PredictorName" in data:
        out["predictor_name"] = data["PredictorName"]
    if "AlgorithmArn" in data:
        out["algorithm_arn"] = data["AlgorithmArn"]
    if "AutoMLAlgorithmArns" in data:
        import aws_sdk_forecast.types.arn_list

        out["auto_ml_algorithm_arns"] = (
            aws_sdk_forecast.types.arn_list.deserialize_aws_json_1_1(
                data["AutoMLAlgorithmArns"]
            )
        )
    if "ForecastHorizon" in data:
        out["forecast_horizon"] = data["ForecastHorizon"]
    if "ForecastTypes" in data:
        import aws_sdk_forecast.types.forecast_types

        out["forecast_types"] = (
            aws_sdk_forecast.types.forecast_types.deserialize_aws_json_1_1(
                data["ForecastTypes"]
            )
        )
    if "PerformAutoML" in data:
        out["perform_auto_ml"] = data["PerformAutoML"]
    if "AutoMLOverrideStrategy" in data:
        import aws_sdk_forecast.types.auto_ml_override_strategy

        out["auto_ml_override_strategy"] = (
            aws_sdk_forecast.types.auto_ml_override_strategy.deserialize_aws_json_1_1(
                data["AutoMLOverrideStrategy"]
            )
        )
    if "PerformHPO" in data:
        out["perform_hpo"] = data["PerformHPO"]
    if "TrainingParameters" in data:
        import aws_sdk_forecast.types.training_parameters

        out["training_parameters"] = (
            aws_sdk_forecast.types.training_parameters.deserialize_aws_json_1_1(
                data["TrainingParameters"]
            )
        )
    if "EvaluationParameters" in data:
        import aws_sdk_forecast.types.evaluation_parameters

        out["evaluation_parameters"] = (
            aws_sdk_forecast.types.evaluation_parameters.deserialize_aws_json_1_1(
                data["EvaluationParameters"]
            )
        )
    if "HPOConfig" in data:
        import aws_sdk_forecast.types.hyper_parameter_tuning_job_config

        out["hpo_config"] = (
            aws_sdk_forecast.types.hyper_parameter_tuning_job_config.deserialize_aws_json_1_1(
                data["HPOConfig"]
            )
        )
    if "InputDataConfig" in data:
        import aws_sdk_forecast.types.input_data_config

        out["input_data_config"] = (
            aws_sdk_forecast.types.input_data_config.deserialize_aws_json_1_1(
                data["InputDataConfig"]
            )
        )
    if "FeaturizationConfig" in data:
        import aws_sdk_forecast.types.featurization_config

        out["featurization_config"] = (
            aws_sdk_forecast.types.featurization_config.deserialize_aws_json_1_1(
                data["FeaturizationConfig"]
            )
        )
    if "EncryptionConfig" in data:
        import aws_sdk_forecast.types.encryption_config

        out["encryption_config"] = (
            aws_sdk_forecast.types.encryption_config.deserialize_aws_json_1_1(
                data["EncryptionConfig"]
            )
        )
    if "PredictorExecutionDetails" in data:
        import aws_sdk_forecast.types.predictor_execution_details

        out["predictor_execution_details"] = (
            aws_sdk_forecast.types.predictor_execution_details.deserialize_aws_json_1_1(
                data["PredictorExecutionDetails"]
            )
        )
    if "EstimatedTimeRemainingInMinutes" in data:
        out["estimated_time_remaining_in_minutes"] = data[
            "EstimatedTimeRemainingInMinutes"
        ]
    if "IsAutoPredictor" in data:
        out["is_auto_predictor"] = data["IsAutoPredictor"]
    if "DatasetImportJobArns" in data:
        import aws_sdk_forecast.types.arn_list

        out["dataset_import_job_arns"] = (
            aws_sdk_forecast.types.arn_list.deserialize_aws_json_1_1(
                data["DatasetImportJobArns"]
            )
        )
    if "Status" in data:
        out["status"] = data["Status"]
    if "Message" in data:
        out["message"] = data["Message"]
    if "CreationTime" in data:
        import aws_sdk_forecast.types.timestamp

        out["creation_time"] = (
            aws_sdk_forecast.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModificationTime" in data:
        import aws_sdk_forecast.types.timestamp

        out["last_modification_time"] = (
            aws_sdk_forecast.types.timestamp.deserialize_aws_json_1_1(
                data["LastModificationTime"]
            )
        )
    if "OptimizationMetric" in data:
        import aws_sdk_forecast.types.optimization_metric

        out["optimization_metric"] = (
            aws_sdk_forecast.types.optimization_metric.deserialize_aws_json_1_1(
                data["OptimizationMetric"]
            )
        )
    return out
