"""Generated from Smithy shape ``com.amazonaws.networkmanager#DeleteCoreNetworkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.core_network_id


class DeleteCoreNetworkRequest(TypedDict, closed=True):
    core_network_id: "aws_sdk_networkmanager.types.core_network_id.CoreNetworkId"
    """<p>The network ID of the deleted core network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCoreNetworkRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCoreNetworkRequest:
    out: DeleteCoreNetworkRequest = {}  # type: ignore[typeddict-item]
    return out
