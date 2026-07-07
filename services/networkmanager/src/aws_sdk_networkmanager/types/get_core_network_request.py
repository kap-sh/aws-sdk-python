"""Generated from Smithy shape ``com.amazonaws.networkmanager#GetCoreNetworkRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.core_network_id


class GetCoreNetworkRequest(TypedDict, closed=True):
    core_network_id: "aws_sdk_networkmanager.types.core_network_id.CoreNetworkId"
    """<p>The ID of a core network.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCoreNetworkRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCoreNetworkRequest:
    out: GetCoreNetworkRequest = {}  # type: ignore[typeddict-item]
    return out
