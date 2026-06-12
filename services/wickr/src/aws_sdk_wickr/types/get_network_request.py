"""Generated from Smithy shape ``com.amazonaws.wickr#GetNetworkRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wickr.types.network_id


class GetNetworkRequest(TypedDict):
    network_id: "aws_sdk_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNetworkRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetNetworkRequest:
    out: GetNetworkRequest = {}  # type: ignore[typeddict-item]
    return out
