"""Generated from Smithy shape ``com.amazonaws.forecast#PredictorSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn
    import aws_sdk_forecast.types.boolean
    import aws_sdk_forecast.types.error_message
    import aws_sdk_forecast.types.name
    import aws_sdk_forecast.types.reference_predictor_summary
    import aws_sdk_forecast.types.status
    import aws_sdk_forecast.types.timestamp


class PredictorSummary(TypedDict):
    predictor_arn: NotRequired["aws_sdk_forecast.types.arn.Arn"]
    """<p>The ARN of the predictor.</p>"""
    predictor_name: NotRequired["aws_sdk_forecast.types.name.Name"]
    """<p>The name of the predictor.</p>"""
    dataset_group_arn: NotRequired["aws_sdk_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the dataset group that contains the data used to train the predictor.</p>"""
    is_auto_predictor: NotRequired["aws_sdk_forecast.types.boolean.Boolean"]
    """<p>Whether AutoPredictor was used to create the predictor.</p>"""
    reference_predictor_summary: NotRequired[
        "aws_sdk_forecast.types.reference_predictor_summary.ReferencePredictorSummary"
    ]
    """<p>A summary of the reference predictor used if the predictor was retrained or upgraded.</p>"""
    status: NotRequired["aws_sdk_forecast.types.status.Status"]
    """<p>The status of the predictor. States include:</p> <ul> <li> <p> <code>ACTIVE</code> </p> </li> <li> <p> <code>CREATE_PENDING</code>, <code>CREATE_IN_PROGRESS</code>, <code>CREATE_FAILED</code> </p> </li> <li> <p> <code>DELETE_PENDING</code>, <code>DELETE_IN_PROGRESS</code>, <code>DELETE_FAILED</code> </p> </li> <li> <p> <code>CREATE_STOPPING</code>, <code>CREATE_STOPPED</code> </p> </li> </ul> <note> <p>The <code>Status</code> of the predictor must be <code>ACTIVE</code> before you can use the predictor to create a forecast.</p> </note>"""
    message: NotRequired["aws_sdk_forecast.types.error_message.ErrorMessage"]
    """<p>If an error occurred, an informational message about the error.</p>"""
    creation_time: NotRequired["aws_sdk_forecast.types.timestamp.Timestamp"]
    """<p>When the model training task was created.</p>"""
    last_modification_time: NotRequired["aws_sdk_forecast.types.timestamp.Timestamp"]
    """<p>The last time the resource was modified. The timestamp depends on the status of the job:</p> <ul> <li> <p> <code>CREATE_PENDING</code> - The <code>CreationTime</code>.</p> </li> <li> <p> <code>CREATE_IN_PROGRESS</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPING</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPED</code> - When the job stopped.</p> </li> <li> <p> <code>ACTIVE</code> or <code>CREATE_FAILED</code> - When the job finished or failed.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PredictorSummary) -> dict:
    out: dict = {}
    if "predictor_arn" in value:
        out["PredictorArn"] = value["predictor_arn"]
    if "predictor_name" in value:
        out["PredictorName"] = value["predictor_name"]
    if "dataset_group_arn" in value:
        out["DatasetGroupArn"] = value["dataset_group_arn"]
    if "is_auto_predictor" in value:
        out["IsAutoPredictor"] = value["is_auto_predictor"]
    if "reference_predictor_summary" in value:
        import aws_sdk_forecast.types.reference_predictor_summary

        out["ReferencePredictorSummary"] = (
            aws_sdk_forecast.types.reference_predictor_summary.serialize_aws_json_1_1(
                value["reference_predictor_summary"]
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
    return out


def deserialize_aws_json_1_1(data: dict) -> PredictorSummary:
    out: PredictorSummary = {}  # type: ignore[typeddict-item]
    if "PredictorArn" in data:
        out["predictor_arn"] = data["PredictorArn"]
    if "PredictorName" in data:
        out["predictor_name"] = data["PredictorName"]
    if "DatasetGroupArn" in data:
        out["dataset_group_arn"] = data["DatasetGroupArn"]
    if "IsAutoPredictor" in data:
        out["is_auto_predictor"] = data["IsAutoPredictor"]
    if "ReferencePredictorSummary" in data:
        import aws_sdk_forecast.types.reference_predictor_summary

        out["reference_predictor_summary"] = (
            aws_sdk_forecast.types.reference_predictor_summary.deserialize_aws_json_1_1(
                data["ReferencePredictorSummary"]
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
    return out
