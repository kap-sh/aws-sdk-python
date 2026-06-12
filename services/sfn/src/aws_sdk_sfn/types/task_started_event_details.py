"""Generated from Smithy shape ``com.amazonaws.sfn#TaskStartedEventDetails``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sfn.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sfn.types.name


class TaskStartedEventDetails(TypedDict):
    resource_type: "aws_sdk_sfn.types.name.Name"
    """<p>The service name of the resource in a task state.</p>"""
    resource: "aws_sdk_sfn.types.name.Name"
    """<p>The action of the resource called by a task state.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TaskStartedEventDetails) -> dict:
    out: dict = {}
    out["resourceType"] = value["resource_type"]
    out["resource"] = value["resource"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TaskStartedEventDetails:
    out: TaskStartedEventDetails = {}  # type: ignore[typeddict-item]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError("TaskStartedEventDetails.resource_type required")
    if "resource" in data:
        out["resource"] = data["resource"]
    else:
        raise DeserializationError("TaskStartedEventDetails.resource required")
    return out
