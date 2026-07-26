"""Generated from Smithy shape ``com.amazonaws.networkmanager#DeleteGlobalNetworkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_networkmanager.types.global_network_id


class DeleteGlobalNetworkRequest(TypedDict, closed=True):
    global_network_id: "capo_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGlobalNetworkRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteGlobalNetworkRequest:
    out: DeleteGlobalNetworkRequest = {}  # type: ignore[typeddict-item]
    return out
