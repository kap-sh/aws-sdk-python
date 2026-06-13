"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#EC2ManagedInstance``."""

from typing import TypedDict

from typing_extensions import NotRequired


class EC2ManagedInstance(TypedDict):
    instance_id: NotRequired["str"]
    """<p>Unique identifier of the managed EC2 instance.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EC2ManagedInstance) -> dict:
    out: dict = {}
    if "instance_id" in value:
        out["InstanceId"] = value["instance_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EC2ManagedInstance:
    out: EC2ManagedInstance = {}  # type: ignore[typeddict-item]
    if "InstanceId" in data:
        out["instance_id"] = data["InstanceId"]
    return out
