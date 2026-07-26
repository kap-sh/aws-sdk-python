"""Generated from Smithy shape ``com.amazonaws.wickr#DeleteNetworkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wickr.types.client_token
    import capo_wickr.types.network_id


class DeleteNetworkRequest(TypedDict, closed=True):
    network_id: "capo_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network to delete.</p>"""
    client_token: NotRequired["capo_wickr.types.client_token.ClientToken"]
    """<p>A unique identifier for this request to ensure idempotency. If you retry a request with the same client token, the service will return the same response without attempting to delete the network again.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteNetworkRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteNetworkRequest:
    out: DeleteNetworkRequest = {}  # type: ignore[typeddict-item]
    return out
