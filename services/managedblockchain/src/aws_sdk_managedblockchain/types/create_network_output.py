"""Generated from Smithy shape ``com.amazonaws.managedblockchain#CreateNetworkOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.resource_id_string


class CreateNetworkOutput(TypedDict):
    network_id: NotRequired[
        "aws_sdk_managedblockchain.types.resource_id_string.ResourceIdString"
    ]
    """<p>The unique identifier for the network.</p>"""
    member_id: NotRequired[
        "aws_sdk_managedblockchain.types.resource_id_string.ResourceIdString"
    ]
    """<p>The unique identifier for the first member within the network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNetworkOutput) -> dict:
    out: dict = {}
    if "network_id" in value:
        out["NetworkId"] = value["network_id"]
    if "member_id" in value:
        out["MemberId"] = value["member_id"]
    return out


def deserialize_json(data: dict) -> CreateNetworkOutput:
    out: CreateNetworkOutput = {}  # type: ignore[typeddict-item]
    if "NetworkId" in data:
        out["network_id"] = data["NetworkId"]
    if "MemberId" in data:
        out["member_id"] = data["MemberId"]
    return out
