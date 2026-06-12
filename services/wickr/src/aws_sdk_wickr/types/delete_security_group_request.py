"""Generated from Smithy shape ``com.amazonaws.wickr#DeleteSecurityGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string
    import aws_sdk_wickr.types.network_id


class DeleteSecurityGroupRequest(TypedDict):
    network_id: "aws_sdk_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network from which the security group will be deleted.</p>"""
    group_id: "aws_sdk_wickr.types.generic_string.GenericString"
    """<p>The unique identifier of the security group to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSecurityGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteSecurityGroupRequest:
    out: DeleteSecurityGroupRequest = {}  # type: ignore[typeddict-item]
    return out
