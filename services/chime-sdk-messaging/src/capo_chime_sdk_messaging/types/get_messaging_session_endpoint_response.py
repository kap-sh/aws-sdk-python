"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#GetMessagingSessionEndpointResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.messaging_session_endpoint


class GetMessagingSessionEndpointResponse(TypedDict, closed=True):
    endpoint: NotRequired[
        "capo_chime_sdk_messaging.types.messaging_session_endpoint.MessagingSessionEndpoint"
    ]
    """<p>The endpoint returned in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMessagingSessionEndpointResponse) -> dict:
    out: dict = {}
    if "endpoint" in value:
        import capo_chime_sdk_messaging.types.messaging_session_endpoint

        out["Endpoint"] = (
            capo_chime_sdk_messaging.types.messaging_session_endpoint.serialize_json(
                value["endpoint"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMessagingSessionEndpointResponse:
    out: GetMessagingSessionEndpointResponse = {}  # type: ignore[typeddict-item]
    if "Endpoint" in data:
        import capo_chime_sdk_messaging.types.messaging_session_endpoint

        out["endpoint"] = (
            capo_chime_sdk_messaging.types.messaging_session_endpoint.deserialize_json(
                data["Endpoint"]
            )
        )
    return out
