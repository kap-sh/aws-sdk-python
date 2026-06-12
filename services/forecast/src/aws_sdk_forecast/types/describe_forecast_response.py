"""Generated from Smithy shape ``com.amazonaws.forecast#DescribeForecastResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn
    import aws_sdk_forecast.types.error_message
    import aws_sdk_forecast.types.forecast_types
    import aws_sdk_forecast.types.long
    import aws_sdk_forecast.types.name
    import aws_sdk_forecast.types.string
    import aws_sdk_forecast.types.time_series_selector
    import aws_sdk_forecast.types.timestamp


class DescribeForecastResponse(TypedDict):
    forecast_arn: NotRequired["aws_sdk_forecast.types.arn.Arn"]
    """<p>The forecast ARN as specified in the request.</p>"""
    forecast_name: NotRequired["aws_sdk_forecast.types.name.Name"]
    """<p>The name of the forecast.</p>"""
    forecast_types: NotRequired["aws_sdk_forecast.types.forecast_types.ForecastTypes"]
    """<p>The quantiles at which probabilistic forecasts were generated.</p>"""
    predictor_arn: NotRequired["aws_sdk_forecast.types.arn.Arn"]
    """<p>The ARN of the predictor used to generate the forecast.</p>"""
    dataset_group_arn: NotRequired["aws_sdk_forecast.types.arn.Arn"]
    """<p>The ARN of the dataset group that provided the data used to train the predictor.</p>"""
    estimated_time_remaining_in_minutes: NotRequired["aws_sdk_forecast.types.long.Long"]
    """<p>The estimated time remaining in minutes for the forecast job to complete.</p>"""
    status: NotRequired["aws_sdk_forecast.types.string.String"]
    """<p>The status of the forecast. States include:</p> <ul> <li> <p> <code>ACTIVE</code> </p> </li> <li> <p> <code>CREATE_PENDING</code>, <code>CREATE_IN_PROGRESS</code>, <code>CREATE_FAILED</code> </p> </li> <li> <p> <code>CREATE_STOPPING</code>, <code>CREATE_STOPPED</code> </p> </li> <li> <p> <code>DELETE_PENDING</code>, <code>DELETE_IN_PROGRESS</code>, <code>DELETE_FAILED</code> </p> </li> </ul> <note> <p>The <code>Status</code> of the forecast must be <code>ACTIVE</code> before you can query or export the forecast.</p> </note>"""
    message: NotRequired["aws_sdk_forecast.types.error_message.ErrorMessage"]
    """<p>If an error occurred, an informational message about the error.</p>"""
    creation_time: NotRequired["aws_sdk_forecast.types.timestamp.Timestamp"]
    """<p>When the forecast creation task was created.</p>"""
    last_modification_time: NotRequired["aws_sdk_forecast.types.timestamp.Timestamp"]
    """<p>The last time the resource was modified. The timestamp depends on the status of the job:</p> <ul> <li> <p> <code>CREATE_PENDING</code> - The <code>CreationTime</code>.</p> </li> <li> <p> <code>CREATE_IN_PROGRESS</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPING</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPED</code> - When the job stopped.</p> </li> <li> <p> <code>ACTIVE</code> or <code>CREATE_FAILED</code> - When the job finished or failed.</p> </li> </ul>"""
    time_series_selector: NotRequired[
        "aws_sdk_forecast.types.time_series_selector.TimeSeriesSelector"
    ]
    """<p>The time series to include in the forecast.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeForecastResponse) -> dict:
    out: dict = {}
    if "forecast_arn" in value:
        out["ForecastArn"] = value["forecast_arn"]
    if "forecast_name" in value:
        out["ForecastName"] = value["forecast_name"]
    if "forecast_types" in value:
        import aws_sdk_forecast.types.forecast_types

        out["ForecastTypes"] = (
            aws_sdk_forecast.types.forecast_types.serialize_aws_json_1_1(
                value["forecast_types"]
            )
        )
    if "predictor_arn" in value:
        out["PredictorArn"] = value["predictor_arn"]
    if "dataset_group_arn" in value:
        out["DatasetGroupArn"] = value["dataset_group_arn"]
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
    if "time_series_selector" in value:
        import aws_sdk_forecast.types.time_series_selector

        out["TimeSeriesSelector"] = (
            aws_sdk_forecast.types.time_series_selector.serialize_aws_json_1_1(
                value["time_series_selector"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeForecastResponse:
    out: DescribeForecastResponse = {}  # type: ignore[typeddict-item]
    if "ForecastArn" in data:
        out["forecast_arn"] = data["ForecastArn"]
    if "ForecastName" in data:
        out["forecast_name"] = data["ForecastName"]
    if "ForecastTypes" in data:
        import aws_sdk_forecast.types.forecast_types

        out["forecast_types"] = (
            aws_sdk_forecast.types.forecast_types.deserialize_aws_json_1_1(
                data["ForecastTypes"]
            )
        )
    if "PredictorArn" in data:
        out["predictor_arn"] = data["PredictorArn"]
    if "DatasetGroupArn" in data:
        out["dataset_group_arn"] = data["DatasetGroupArn"]
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
    if "TimeSeriesSelector" in data:
        import aws_sdk_forecast.types.time_series_selector

        out["time_series_selector"] = (
            aws_sdk_forecast.types.time_series_selector.deserialize_aws_json_1_1(
                data["TimeSeriesSelector"]
            )
        )
    return out
