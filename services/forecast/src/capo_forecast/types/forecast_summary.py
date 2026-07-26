"""Generated from Smithy shape ``com.amazonaws.forecast#ForecastSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_forecast.types.arn
    import capo_forecast.types.boolean
    import capo_forecast.types.error_message
    import capo_forecast.types.name
    import capo_forecast.types.status
    import capo_forecast.types.string
    import capo_forecast.types.timestamp


class ForecastSummary(TypedDict, closed=True):
    forecast_arn: NotRequired["capo_forecast.types.arn.Arn"]
    """<p>The ARN of the forecast.</p>"""
    forecast_name: NotRequired["capo_forecast.types.name.Name"]
    """<p>The name of the forecast.</p>"""
    predictor_arn: NotRequired["capo_forecast.types.string.String"]
    """<p>The ARN of the predictor used to generate the forecast.</p>"""
    created_using_auto_predictor: NotRequired["capo_forecast.types.boolean.Boolean"]
    """<p>Whether the Forecast was created from an AutoPredictor.</p>"""
    dataset_group_arn: NotRequired["capo_forecast.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the dataset group that provided the data used to train the predictor.</p>"""
    status: NotRequired["capo_forecast.types.status.Status"]
    """<p>The status of the forecast. States include:</p> <ul> <li> <p> <code>ACTIVE</code> </p> </li> <li> <p> <code>CREATE_PENDING</code>, <code>CREATE_IN_PROGRESS</code>, <code>CREATE_FAILED</code> </p> </li> <li> <p> <code>CREATE_STOPPING</code>, <code>CREATE_STOPPED</code> </p> </li> <li> <p> <code>DELETE_PENDING</code>, <code>DELETE_IN_PROGRESS</code>, <code>DELETE_FAILED</code> </p> </li> </ul> <note> <p>The <code>Status</code> of the forecast must be <code>ACTIVE</code> before you can query or export the forecast.</p> </note>"""
    message: NotRequired["capo_forecast.types.error_message.ErrorMessage"]
    """<p>If an error occurred, an informational message about the error.</p>"""
    creation_time: NotRequired["capo_forecast.types.timestamp.Timestamp"]
    """<p>When the forecast creation task was created.</p>"""
    last_modification_time: NotRequired["capo_forecast.types.timestamp.Timestamp"]
    """<p>The last time the resource was modified. The timestamp depends on the status of the job:</p> <ul> <li> <p> <code>CREATE_PENDING</code> - The <code>CreationTime</code>.</p> </li> <li> <p> <code>CREATE_IN_PROGRESS</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPING</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPED</code> - When the job stopped.</p> </li> <li> <p> <code>ACTIVE</code> or <code>CREATE_FAILED</code> - When the job finished or failed.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ForecastSummary) -> dict:
    out: dict = {}
    if "forecast_arn" in value:
        out["ForecastArn"] = value["forecast_arn"]
    if "forecast_name" in value:
        out["ForecastName"] = value["forecast_name"]
    if "predictor_arn" in value:
        out["PredictorArn"] = value["predictor_arn"]
    if "created_using_auto_predictor" in value:
        out["CreatedUsingAutoPredictor"] = value["created_using_auto_predictor"]
    if "dataset_group_arn" in value:
        out["DatasetGroupArn"] = value["dataset_group_arn"]
    if "status" in value:
        out["Status"] = value["status"]
    if "message" in value:
        out["Message"] = value["message"]
    if "creation_time" in value:
        import capo_forecast.types.timestamp

        out["CreationTime"] = capo_forecast.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modification_time" in value:
        import capo_forecast.types.timestamp

        out["LastModificationTime"] = (
            capo_forecast.types.timestamp.serialize_aws_json_1_1(
                value["last_modification_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ForecastSummary:
    out: ForecastSummary = {}  # type: ignore[typeddict-item]
    if "ForecastArn" in data:
        out["forecast_arn"] = data["ForecastArn"]
    if "ForecastName" in data:
        out["forecast_name"] = data["ForecastName"]
    if "PredictorArn" in data:
        out["predictor_arn"] = data["PredictorArn"]
    if "CreatedUsingAutoPredictor" in data:
        out["created_using_auto_predictor"] = data["CreatedUsingAutoPredictor"]
    if "DatasetGroupArn" in data:
        out["dataset_group_arn"] = data["DatasetGroupArn"]
    if "Status" in data:
        out["status"] = data["Status"]
    if "Message" in data:
        out["message"] = data["Message"]
    if "CreationTime" in data:
        import capo_forecast.types.timestamp

        out["creation_time"] = capo_forecast.types.timestamp.deserialize_aws_json_1_1(
            data["CreationTime"]
        )
    if "LastModificationTime" in data:
        import capo_forecast.types.timestamp

        out["last_modification_time"] = (
            capo_forecast.types.timestamp.deserialize_aws_json_1_1(
                data["LastModificationTime"]
            )
        )
    return out
