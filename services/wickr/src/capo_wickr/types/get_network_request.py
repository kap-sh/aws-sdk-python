"""Generated from Smithy shape ``com.amazonaws.wickr#GetNetworkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.network_id


class GetNetworkRequest(TypedDict, closed=True):
    network_id: "capo_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNetworkRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetNetworkRequest:
    out: GetNetworkRequest = {}  # type: ignore[typeddict-item]
    return out
