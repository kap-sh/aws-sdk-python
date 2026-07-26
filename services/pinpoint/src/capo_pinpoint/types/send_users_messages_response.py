"""Generated from Smithy shape ``com.amazonaws.pinpoint#SendUsersMessagesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.send_users_message_response


class SendUsersMessagesResponse(TypedDict, closed=True):
    send_users_message_response: NotRequired[
        "capo_pinpoint.types.send_users_message_response.SendUsersMessageResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: SendUsersMessagesResponse) -> dict:
    out: dict = {}
    if "send_users_message_response" in value:
        import capo_pinpoint.types.send_users_message_response

        out["SendUsersMessageResponse"] = (
            capo_pinpoint.types.send_users_message_response.serialize_json(
                value["send_users_message_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> SendUsersMessagesResponse:
    out: SendUsersMessagesResponse = {}  # type: ignore[typeddict-item]
    if "SendUsersMessageResponse" in data:
        import capo_pinpoint.types.send_users_message_response

        out["send_users_message_response"] = (
            capo_pinpoint.types.send_users_message_response.deserialize_json(
                data["SendUsersMessageResponse"]
            )
        )
    return out
