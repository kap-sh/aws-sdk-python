"""Generated from Smithy shape ``com.amazonaws.wickr#GetNetworkSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_wickr.types.network_id


class GetNetworkSettingsRequest(TypedDict, closed=True):
    network_id: "aws_sdk_wickr.types.network_id.NetworkId"
    """<p>The ID of the Wickr network whose settings will be retrieved.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNetworkSettingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetNetworkSettingsRequest:
    out: GetNetworkSettingsRequest = {}  # type: ignore[typeddict-item]
    return out
