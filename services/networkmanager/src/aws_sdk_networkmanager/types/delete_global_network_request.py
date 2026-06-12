"""Generated from Smithy shape ``com.amazonaws.networkmanager#DeleteGlobalNetworkRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.global_network_id


class DeleteGlobalNetworkRequest(TypedDict):
    global_network_id: "aws_sdk_networkmanager.types.global_network_id.GlobalNetworkId"
    """<p>The ID of the global network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGlobalNetworkRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteGlobalNetworkRequest:
    out: DeleteGlobalNetworkRequest = {}  # type: ignore[typeddict-item]
    return out
