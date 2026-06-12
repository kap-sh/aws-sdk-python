"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#GetMessagingSessionEndpointResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_messaging.types.messaging_session_endpoint


class GetMessagingSessionEndpointResponse(TypedDict):
    endpoint: NotRequired[
        "aws_sdk_chime_sdk_messaging.types.messaging_session_endpoint.MessagingSessionEndpoint"
    ]
    """<p>The endpoint returned in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMessagingSessionEndpointResponse) -> dict:
    out: dict = {}
    if "endpoint" in value:
        import aws_sdk_chime_sdk_messaging.types.messaging_session_endpoint

        out["Endpoint"] = (
            aws_sdk_chime_sdk_messaging.types.messaging_session_endpoint.serialize_json(
                value["endpoint"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMessagingSessionEndpointResponse:
    out: GetMessagingSessionEndpointResponse = {}  # type: ignore[typeddict-item]
    if "Endpoint" in data:
        import aws_sdk_chime_sdk_messaging.types.messaging_session_endpoint

        out["endpoint"] = (
            aws_sdk_chime_sdk_messaging.types.messaging_session_endpoint.deserialize_json(
                data["Endpoint"]
            )
        )
    return out
