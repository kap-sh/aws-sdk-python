"""Generated from Smithy shape ``com.amazonaws.wickr#GetSecurityGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wickr.types.generic_string
    import aws_sdk_wickr.types.network_id


class GetSecurityGroupRequest(TypedDict):
    network_id: "aws_sdk_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network containing the security group.</p>"""
    group_id: "aws_sdk_wickr.types.generic_string.GenericString"
    """<p>The unique identifier of the security group to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSecurityGroupRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSecurityGroupRequest:
    out: GetSecurityGroupRequest = {}  # type: ignore[typeddict-item]
    return out
