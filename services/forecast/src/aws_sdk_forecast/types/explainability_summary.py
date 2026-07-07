"""Generated from Smithy shape ``com.amazonaws.forecast#ExplainabilitySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_forecast.types.arn
    import aws_sdk_forecast.types.explainability_config
    import aws_sdk_forecast.types.message
    import aws_sdk_forecast.types.name
    import aws_sdk_forecast.types.status
    import aws_sdk_forecast.types.timestamp


class ExplainabilitySummary(TypedDict, closed=True):
    explainability_arn: NotRequired["aws_sdk_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the Explainability.</p>"""
    explainability_name: NotRequired["aws_sdk_forecast.types.name.Name"]
    """<p>The name of the Explainability.</p>"""
    resource_arn: NotRequired["aws_sdk_forecast.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the Predictor or Forecast used to create the Explainability.</p>"""
    explainability_config: NotRequired[
        "aws_sdk_forecast.types.explainability_config.ExplainabilityConfig"
    ]
    """<p>The configuration settings that define the granularity of time series and time points for the Explainability.</p>"""
    status: NotRequired["aws_sdk_forecast.types.status.Status"]
    """<p>The status of the Explainability. States include: </p> <ul> <li> <p> <code>ACTIVE</code> </p> </li> <li> <p> <code>CREATE_PENDING</code>, <code>CREATE_IN_PROGRESS</code>, <code>CREATE_FAILED</code> </p> </li> <li> <p> <code>CREATE_STOPPING</code>, <code>CREATE_STOPPED</code> </p> </li> <li> <p> <code>DELETE_PENDING</code>, <code>DELETE_IN_PROGRESS</code>, <code>DELETE_FAILED</code> </p> </li> </ul>"""
    message: NotRequired["aws_sdk_forecast.types.message.Message"]
    """<p>Information about any errors that may have occurred during the Explainability creation process.</p>"""
    creation_time: NotRequired["aws_sdk_forecast.types.timestamp.Timestamp"]
    """<p>When the Explainability was created.</p>"""
    last_modification_time: NotRequired["aws_sdk_forecast.types.timestamp.Timestamp"]
    """<p>The last time the resource was modified. The timestamp depends on the status of the job:</p> <ul> <li> <p> <code>CREATE_PENDING</code> - The <code>CreationTime</code>.</p> </li> <li> <p> <code>CREATE_IN_PROGRESS</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPING</code> - The current timestamp.</p> </li> <li> <p> <code>CREATE_STOPPED</code> - When the job stopped.</p> </li> <li> <p> <code>ACTIVE</code> or <code>CREATE_FAILED</code> - When the job finished or failed.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExplainabilitySummary) -> dict:
    out: dict = {}
    if "explainability_arn" in value:
        out["ExplainabilityArn"] = value["explainability_arn"]
    if "explainability_name" in value:
        out["ExplainabilityName"] = value["explainability_name"]
    if "resource_arn" in value:
        out["ResourceArn"] = value["resource_arn"]
    if "explainability_config" in value:
        import aws_sdk_forecast.types.explainability_config

        out["ExplainabilityConfig"] = (
            aws_sdk_forecast.types.explainability_config.serialize_aws_json_1_1(
                value["explainability_config"]
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


def deserialize_aws_json_1_1(data: dict) -> ExplainabilitySummary:
    out: ExplainabilitySummary = {}  # type: ignore[typeddict-item]
    if "ExplainabilityArn" in data:
        out["explainability_arn"] = data["ExplainabilityArn"]
    if "ExplainabilityName" in data:
        out["explainability_name"] = data["ExplainabilityName"]
    if "ResourceArn" in data:
        out["resource_arn"] = data["ResourceArn"]
    if "ExplainabilityConfig" in data:
        import aws_sdk_forecast.types.explainability_config

        out["explainability_config"] = (
            aws_sdk_forecast.types.explainability_config.deserialize_aws_json_1_1(
                data["ExplainabilityConfig"]
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
