"""Generated from Smithy shape ``com.amazonaws.wickr#DeleteNetworkRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wickr.types.client_token
    import aws_sdk_wickr.types.network_id


class DeleteNetworkRequest(TypedDict):
    network_id: "aws_sdk_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network to delete.</p>"""
    client_token: NotRequired["aws_sdk_wickr.types.client_token.ClientToken"]
    """<p>A unique identifier for this request to ensure idempotency. If you retry a request with the same client token, the service will return the same response without attempting to delete the network again.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteNetworkRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteNetworkRequest:
    out: DeleteNetworkRequest = {}  # type: ignore[typeddict-item]
    return out
