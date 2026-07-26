"""Generated from Smithy shape ``com.amazonaws.pinpoint#SendUsersMessagesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.send_users_message_request


class SendUsersMessagesRequest(TypedDict, closed=True):
    application_id: "capo_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    send_users_message_request: NotRequired[
        "capo_pinpoint.types.send_users_message_request.SendUsersMessageRequest"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: SendUsersMessagesRequest) -> dict:
    out: dict = {}
    if "send_users_message_request" in value:
        import capo_pinpoint.types.send_users_message_request

        out["SendUsersMessageRequest"] = (
            capo_pinpoint.types.send_users_message_request.serialize_json(
                value["send_users_message_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> SendUsersMessagesRequest:
    out: SendUsersMessagesRequest = {}  # type: ignore[typeddict-item]
    if "SendUsersMessageRequest" in data:
        import capo_pinpoint.types.send_users_message_request

        out["send_users_message_request"] = (
            capo_pinpoint.types.send_users_message_request.deserialize_json(
                data["SendUsersMessageRequest"]
            )
        )
    return out
