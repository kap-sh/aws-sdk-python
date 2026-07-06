"""Generated from Smithy shape ``com.amazonaws.sfn#TaskTimedOutEventDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.name
    import aws_sdk_sfn.types.sensitive_cause
    import aws_sdk_sfn.types.sensitive_error


class TaskTimedOutEventDetails(TypedDict, closed=True):
    resource_type: "aws_sdk_sfn.types.name.Name"
    """<p>The service name of the resource in a task state.</p>"""
    resource: "aws_sdk_sfn.types.name.Name"
    """<p>The action of the resource called by a task state.</p>"""
    error: NotRequired["aws_sdk_sfn.types.sensitive_error.SensitiveError"]
    """<p>The error code of the failure.</p>"""
    cause: NotRequired["aws_sdk_sfn.types.sensitive_cause.SensitiveCause"]
    """<p>A more detailed explanation of the cause of the failure.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TaskTimedOutEventDetails) -> dict:
    out: dict = {}
    out["resourceType"] = value["resource_type"]
    out["resource"] = value["resource"]
    if "error" in value:
        out["error"] = value["error"]
    if "cause" in value:
        out["cause"] = value["cause"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TaskTimedOutEventDetails:
    out: TaskTimedOutEventDetails = {}  # type: ignore[typeddict-item]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError("TaskTimedOutEventDetails.resource_type required")
    if "resource" in data:
        out["resource"] = data["resource"]
    else:
        raise DeserializationError("TaskTimedOutEventDetails.resource required")
    if "error" in data:
        out["error"] = data["error"]
    if "cause" in data:
        out["cause"] = data["cause"]
    return out
