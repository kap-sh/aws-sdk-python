"""Generated from Smithy shape ``com.amazonaws.forecast#DescribeAutoPredictorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn
    import aws_sdk_forecast.types.arn_list
    import aws_sdk_forecast.types.data_config
    import aws_sdk_forecast.types.encryption_config
    import aws_sdk_forecast.types.explainability_info
    import aws_sdk_forecast.types.forecast_dimensions
    import aws_sdk_forecast.types.forecast_types
    import aws_sdk_forecast.types.frequency
    import aws_sdk_forecast.types.integer
    import aws_sdk_forecast.types.long
    import aws_sdk_forecast.types.message
    import aws_sdk_forecast.types.monitor_info
    import aws_sdk_forecast.types.name
    import aws_sdk_forecast.types.optimization_metric
    import aws_sdk_forecast.types.reference_predictor_summary
    import aws_sdk_forecast.types.status
    import aws_sdk_forecast.types.time_alignment_boundary
    import aws_sdk_forecast.types.timestamp


class DescribeAutoPredictorResponse(TypedDict, closed=True):
    predictor_arn: NotRequired["aws_sdk_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the predictor</p>"""
    predictor_name: NotRequired["aws_sdk_forecast.types.name.Name"]
    """<p>The name of the predictor.</p>"""
    forecast_horizon: NotRequired["aws_sdk_forecast.types.integer.Integer"]
    """<p>The number of time-steps that the model predicts. The forecast horizon is also called the prediction length.</p>"""
    forecast_types: NotRequired["aws_sdk_forecast.types.forecast_types.ForecastTypes"]
    r"""<p>The forecast types used during predictor training. Default value is [\"0.1\",\"0.5\",\"0.9\"].</p>"""
    forecast_frequency: NotRequired["aws_sdk_forecast.types.frequency.Frequency"]
    r"""<p>The frequency of predictions in a forecast.</p> <p>Valid intervals are Y (Year), M (Month), W (Week), D (Day), H (Hour), 30min (30 minutes), 15min (15 minutes), 10min (10 minutes), 5min (5 minutes), and 1min (1 minute). For example, \"Y\" indicates every year and \"5min\" indicates every five minutes.</p>"""
    forecast_dimensions: NotRequired[
        "aws_sdk_forecast.types.forecast_dimensions.ForecastDimensions"
    ]
    """<p>An array of dimension (field) names that specify the attributes used to group your time series.</p>"""
    dataset_import_job_arns: NotRequired["aws_sdk_forecast.types.arn_list.ArnList"]
    """<p>An array of the ARNs of the dataset import jobs used to import training data for the predictor.</p>"""
    data_config: NotRequired["aws_sdk_forecast.types.data_config.DataConfig"]
    """<p>The data configuration for your dataset group and any additional datasets.</p>"""
    encryption_config: NotRequired[
        "aws_sdk_forecast.types.encryption_config.EncryptionConfig"
    ]
    reference_predictor_summary: NotRequired[
        "aws_sdk_forecast.types.reference_predictor_summary.ReferencePredictorSummary"
    ]
    """<p>The ARN and state of the reference predictor. This parameter is only valid for retrained or upgraded predictors.</p>"""
    estimated_time_remaining_in_minutes: NotRequired["aws_sdk_forecast.types.long.Long"]
    """<p>The estimated time remaining in minutes for the predictor training job to complete.</p>"""
    status: NotRequired["aws_sdk_forecast.types.status.Status"]
    """<p>The status of the predictor. States include: </p> <ul> <li> <p> <code>ACTIVE</code> </p> </li> <li> <p> <code>CREATE_PENDING</code>, <code>CREATE_IN_PROGRESS</code>, <code>CREATE_FAILED</code> </p> </li> <li> <p> <code>CREATE_STOPPING</code>, <code>CREATE_STOPPED</code> </p> </li> <li> <p> <code>DELETE_PENDING</code>, <code>DELETE_IN_PROGRESS</code>, <code>DELETE_FAILED</code> </p> </li> </ul>"""
    message: NotRequired["aws_sdk_forecast.types.message.Message"]
    """<p>In the event of an error, a message detailing the cause of the error.</p>"""
    creation_time: NotRequired["aws_sdk_forecast.types.timestamp.Timestamp"]
    """<p>The timestamp of the CreateAutoPredictor request.</p>"""
    last_modification_time: NotRequired["aws_sdk_forecast.types.timestamp.Timestamp"]
    """<p>The last time the resource was modified. The timestamp depends on the status of the job:</p> <ul> <li> <p> <code>CREATE_PENDING</code> - The <code>CreationTime</code>.</p> </li> <li> <p> <code>CREATE_IN_PROGRESS</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPING</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPED</code> - When the job stopped.</p> </li> <li> <p> <code>ACTIVE</code> or <code>CREATE_FAILED</code> - When the job finished or failed.</p> </li> </ul>"""
    optimization_metric: NotRequired[
        "aws_sdk_forecast.types.optimization_metric.OptimizationMetric"
    ]
    """<p>The accuracy metric used to optimize the predictor.</p>"""
    explainability_info: NotRequired[
        "aws_sdk_forecast.types.explainability_info.ExplainabilityInfo"
    ]
    """<p>Provides the status and ARN of the Predictor Explainability.</p>"""
    monitor_info: NotRequired["aws_sdk_forecast.types.monitor_info.MonitorInfo"]
    """<p>A object with the Amazon Resource Name (ARN) and status of the monitor resource.</p>"""
    time_alignment_boundary: NotRequired[
        "aws_sdk_forecast.types.time_alignment_boundary.TimeAlignmentBoundary"
    ]
    """<p>The time boundary Forecast uses when aggregating data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAutoPredictorResponse) -> dict:
    out: dict = {}
    if "predictor_arn" in value:
        out["PredictorArn"] = value["predictor_arn"]
    if "predictor_name" in value:
        out["PredictorName"] = value["predictor_name"]
    if "forecast_horizon" in value:
        out["ForecastHorizon"] = value["forecast_horizon"]
    if "forecast_types" in value:
        import aws_sdk_forecast.types.forecast_types

        out["ForecastTypes"] = (
            aws_sdk_forecast.types.forecast_types.serialize_aws_json_1_1(
                value["forecast_types"]
            )
        )
    if "forecast_frequency" in value:
        out["ForecastFrequency"] = value["forecast_frequency"]
    if "forecast_dimensions" in value:
        import aws_sdk_forecast.types.forecast_dimensions

        out["ForecastDimensions"] = (
            aws_sdk_forecast.types.forecast_dimensions.serialize_aws_json_1_1(
                value["forecast_dimensions"]
            )
        )
    if "dataset_import_job_arns" in value:
        import aws_sdk_forecast.types.arn_list

        out["DatasetImportJobArns"] = (
            aws_sdk_forecast.types.arn_list.serialize_aws_json_1_1(
                value["dataset_import_job_arns"]
            )
        )
    if "data_config" in value:
        import aws_sdk_forecast.types.data_config

        out["DataConfig"] = aws_sdk_forecast.types.data_config.serialize_aws_json_1_1(
            value["data_config"]
        )
    if "encryption_config" in value:
        import aws_sdk_forecast.types.encryption_config

        out["EncryptionConfig"] = (
            aws_sdk_forecast.types.encryption_config.serialize_aws_json_1_1(
                value["encryption_config"]
            )
        )
    if "reference_predictor_summary" in value:
        import aws_sdk_forecast.types.reference_predictor_summary

        out["ReferencePredictorSummary"] = (
            aws_sdk_forecast.types.reference_predictor_summary.serialize_aws_json_1_1(
                value["reference_predictor_summary"]
            )
        )
    if "estimated_time_remaining_in_minutes" in value:
        out["EstimatedTimeRemainingInMinutes"] = value[
            "estimated_time_remaining_in_minutes"
        ]
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
    if "explainability_info" in value:
        import aws_sdk_forecast.types.explainability_info

        out["ExplainabilityInfo"] = (
            aws_sdk_forecast.types.explainability_info.serialize_aws_json_1_1(
                value["explainability_info"]
            )
        )
    if "monitor_info" in value:
        import aws_sdk_forecast.types.monitor_info

        out["MonitorInfo"] = aws_sdk_forecast.types.monitor_info.serialize_aws_json_1_1(
            value["monitor_info"]
        )
    if "time_alignment_boundary" in value:
        import aws_sdk_forecast.types.time_alignment_boundary

        out["TimeAlignmentBoundary"] = (
            aws_sdk_forecast.types.time_alignment_boundary.serialize_aws_json_1_1(
                value["time_alignment_boundary"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAutoPredictorResponse:
    out: DescribeAutoPredictorResponse = {}  # type: ignore[typeddict-item]
    if "PredictorArn" in data:
        out["predictor_arn"] = data["PredictorArn"]
    if "PredictorName" in data:
        out["predictor_name"] = data["PredictorName"]
    if "ForecastHorizon" in data:
        out["forecast_horizon"] = data["ForecastHorizon"]
    if "ForecastTypes" in data:
        import aws_sdk_forecast.types.forecast_types

        out["forecast_types"] = (
            aws_sdk_forecast.types.forecast_types.deserialize_aws_json_1_1(
                data["ForecastTypes"]
            )
        )
    if "ForecastFrequency" in data:
        out["forecast_frequency"] = data["ForecastFrequency"]
    if "ForecastDimensions" in data:
        import aws_sdk_forecast.types.forecast_dimensions

        out["forecast_dimensions"] = (
            aws_sdk_forecast.types.forecast_dimensions.deserialize_aws_json_1_1(
                data["ForecastDimensions"]
            )
        )
    if "DatasetImportJobArns" in data:
        import aws_sdk_forecast.types.arn_list

        out["dataset_import_job_arns"] = (
            aws_sdk_forecast.types.arn_list.deserialize_aws_json_1_1(
                data["DatasetImportJobArns"]
            )
        )
    if "DataConfig" in data:
        import aws_sdk_forecast.types.data_config

        out["data_config"] = (
            aws_sdk_forecast.types.data_config.deserialize_aws_json_1_1(
                data["DataConfig"]
            )
        )
    if "EncryptionConfig" in data:
        import aws_sdk_forecast.types.encryption_config

        out["encryption_config"] = (
            aws_sdk_forecast.types.encryption_config.deserialize_aws_json_1_1(
                data["EncryptionConfig"]
            )
        )
    if "ReferencePredictorSummary" in data:
        import aws_sdk_forecast.types.reference_predictor_summary

        out["reference_predictor_summary"] = (
            aws_sdk_forecast.types.reference_predictor_summary.deserialize_aws_json_1_1(
                data["ReferencePredictorSummary"]
            )
        )
    if "EstimatedTimeRemainingInMinutes" in data:
        out["estimated_time_remaining_in_minutes"] = data[
            "EstimatedTimeRemainingInMinutes"
        ]
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
    if "ExplainabilityInfo" in data:
        import aws_sdk_forecast.types.explainability_info

        out["explainability_info"] = (
            aws_sdk_forecast.types.explainability_info.deserialize_aws_json_1_1(
                data["ExplainabilityInfo"]
            )
        )
    if "MonitorInfo" in data:
        import aws_sdk_forecast.types.monitor_info

        out["monitor_info"] = (
            aws_sdk_forecast.types.monitor_info.deserialize_aws_json_1_1(
                data["MonitorInfo"]
            )
        )
    if "TimeAlignmentBoundary" in data:
        import aws_sdk_forecast.types.time_alignment_boundary

        out["time_alignment_boundary"] = (
            aws_sdk_forecast.types.time_alignment_boundary.deserialize_aws_json_1_1(
                data["TimeAlignmentBoundary"]
            )
        )
    return out
