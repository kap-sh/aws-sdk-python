"""Generated from Smithy shape ``com.amazonaws.sfn#TaskScheduledEventDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.connector_parameters
    import aws_sdk_sfn.types.name
    import aws_sdk_sfn.types.task_credentials
    import aws_sdk_sfn.types.timeout_in_seconds


class TaskScheduledEventDetails(TypedDict, closed=True):
    resource_type: "aws_sdk_sfn.types.name.Name"
    """<p>The service name of the resource in a task state.</p>"""
    resource: "aws_sdk_sfn.types.name.Name"
    """<p>The action of the resource called by a task state.</p>"""
    region: "aws_sdk_sfn.types.name.Name"
    """<p>The region of the scheduled task</p>"""
    parameters: "aws_sdk_sfn.types.connector_parameters.ConnectorParameters"
    """<p>The JSON data passed to the resource referenced in a task state. Length constraints apply to the payload size, and are expressed as bytes in UTF-8 encoding.</p>"""
    timeout_in_seconds: NotRequired[
        "aws_sdk_sfn.types.timeout_in_seconds.TimeoutInSeconds"
    ]
    """<p>The maximum allowed duration of the task.</p>"""
    heartbeat_in_seconds: NotRequired[
        "aws_sdk_sfn.types.timeout_in_seconds.TimeoutInSeconds"
    ]
    """<p>The maximum allowed duration between two heartbeats for the task.</p>"""
    task_credentials: NotRequired["aws_sdk_sfn.types.task_credentials.TaskCredentials"]
    """<p>The credentials that Step Functions uses for the task.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TaskScheduledEventDetails) -> dict:
    out: dict = {}
    out["resourceType"] = value["resource_type"]
    out["resource"] = value["resource"]
    out["region"] = value["region"]
    out["parameters"] = value["parameters"]
    if "timeout_in_seconds" in value:
        out["timeoutInSeconds"] = value["timeout_in_seconds"]
    if "heartbeat_in_seconds" in value:
        out["heartbeatInSeconds"] = value["heartbeat_in_seconds"]
    if "task_credentials" in value:
        import aws_sdk_sfn.types.task_credentials

        out["taskCredentials"] = (
            aws_sdk_sfn.types.task_credentials.serialize_aws_json_1_0(
                value["task_credentials"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TaskScheduledEventDetails:
    out: TaskScheduledEventDetails = {}  # type: ignore[typeddict-item]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError("TaskScheduledEventDetails.resource_type required")
    if "resource" in data:
        out["resource"] = data["resource"]
    else:
        raise DeserializationError("TaskScheduledEventDetails.resource required")
    if "region" in data:
        out["region"] = data["region"]
    else:
        raise DeserializationError("TaskScheduledEventDetails.region required")
    if "parameters" in data:
        out["parameters"] = data["parameters"]
    else:
        raise DeserializationError("TaskScheduledEventDetails.parameters required")
    if "timeoutInSeconds" in data:
        out["timeout_in_seconds"] = data["timeoutInSeconds"]
    if "heartbeatInSeconds" in data:
        out["heartbeat_in_seconds"] = data["heartbeatInSeconds"]
    if "taskCredentials" in data:
        import aws_sdk_sfn.types.task_credentials

        out["task_credentials"] = (
            aws_sdk_sfn.types.task_credentials.deserialize_aws_json_1_0(
                data["taskCredentials"]
            )
        )
    return out
