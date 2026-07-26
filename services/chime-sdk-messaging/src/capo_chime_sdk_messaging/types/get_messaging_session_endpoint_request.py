"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#GetMessagingSessionEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.network_type


class GetMessagingSessionEndpointRequest(TypedDict, closed=True):
    network_type: NotRequired["capo_chime_sdk_messaging.types.network_type.NetworkType"]
    """<p>The type of network for the messaging session endpoint. Either IPv4 only or dual-stack (IPv4 and IPv6).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMessagingSessionEndpointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMessagingSessionEndpointRequest:
    out: GetMessagingSessionEndpointRequest = {}  # type: ignore[typeddict-item]
    return out
