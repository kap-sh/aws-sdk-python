"""Generated from Smithy shape ``com.amazonaws.managedblockchain#GetNetworkInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_managedblockchain.types.resource_id_string


class GetNetworkInput(TypedDict):
    network_id: "aws_sdk_managedblockchain.types.resource_id_string.ResourceIdString"
    """<p>The unique identifier of the network to get information about.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNetworkInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetNetworkInput:
    out: GetNetworkInput = {}  # type: ignore[typeddict-item]
    return out
