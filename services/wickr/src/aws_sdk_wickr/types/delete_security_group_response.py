"""Generated from Smithy shape ``com.amazonaws.wickr#DeleteSecurityGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string
    import aws_sdk_wickr.types.network_id


class DeleteSecurityGroupResponse(TypedDict):
    message: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>A message indicating the result of the security group deletion operation.</p>"""
    network_id: NotRequired["aws_sdk_wickr.types.network_id.NetworkId"]
    """<p>The ID of the network from which the security group was deleted.</p>"""
    group_id: NotRequired["aws_sdk_wickr.types.generic_string.GenericString"]
    """<p>The ID of the security group that was deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSecurityGroupResponse) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    if "network_id" in value:
        out["networkId"] = value["network_id"]
    if "group_id" in value:
        out["groupId"] = value["group_id"]
    return out


def deserialize_json(data: dict) -> DeleteSecurityGroupResponse:
    out: DeleteSecurityGroupResponse = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    if "networkId" in data:
        out["network_id"] = data["networkId"]
    if "groupId" in data:
        out["group_id"] = data["groupId"]
    return out
