"""Generated from Smithy shape ``com.amazonaws.sfn#TaskStartFailedEventDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sfn.types.name
    import capo_sfn.types.sensitive_cause
    import capo_sfn.types.sensitive_error


class TaskStartFailedEventDetails(TypedDict, closed=True):
    resource_type: "capo_sfn.types.name.Name"
    """<p>The service name of the resource in a task state.</p>"""
    resource: "capo_sfn.types.name.Name"
    """<p>The action of the resource called by a task state.</p>"""
    error: NotRequired["capo_sfn.types.sensitive_error.SensitiveError"]
    """<p>The error code of the failure.</p>"""
    cause: NotRequired["capo_sfn.types.sensitive_cause.SensitiveCause"]
    """<p>A more detailed explanation of the cause of the failure.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TaskStartFailedEventDetails) -> dict:
    out: dict = {}
    out["resourceType"] = value["resource_type"]
    out["resource"] = value["resource"]
    if "error" in value:
        out["error"] = value["error"]
    if "cause" in value:
        out["cause"] = value["cause"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TaskStartFailedEventDetails:
    out: TaskStartFailedEventDetails = {}  # type: ignore[typeddict-item]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError("TaskStartFailedEventDetails.resource_type required")
    if "resource" in data:
        out["resource"] = data["resource"]
    else:
        raise DeserializationError("TaskStartFailedEventDetails.resource required")
    if "error" in data:
        out["error"] = data["error"]
    if "cause" in data:
        out["cause"] = data["cause"]
    return out
