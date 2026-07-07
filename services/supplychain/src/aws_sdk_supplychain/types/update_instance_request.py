"""Generated from Smithy shape ``com.amazonaws.supplychain#UpdateInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_supplychain.types.instance_description
    import aws_sdk_supplychain.types.instance_name
    import aws_sdk_supplychain.types.uuid


class UpdateInstanceRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_supplychain.types.uuid.UUID"
    """<p>The AWS Supply Chain instance identifier.</p>"""
    instance_name: NotRequired["aws_sdk_supplychain.types.instance_name.InstanceName"]
    """<p>The AWS Supply Chain instance name.</p>"""
    instance_description: NotRequired[
        "aws_sdk_supplychain.types.instance_description.InstanceDescription"
    ]
    """<p>The AWS Supply Chain instance description.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateInstanceRequest) -> dict:
    out: dict = {}
    if "instance_name" in value:
        out["instanceName"] = value["instance_name"]
    if "instance_description" in value:
        out["instanceDescription"] = value["instance_description"]
    return out


def deserialize_json(data: dict) -> UpdateInstanceRequest:
    out: UpdateInstanceRequest = {}  # type: ignore[typeddict-item]
    if "instanceName" in data:
        out["instance_name"] = data["instanceName"]
    if "instanceDescription" in data:
        out["instance_description"] = data["instanceDescription"]
    return out
