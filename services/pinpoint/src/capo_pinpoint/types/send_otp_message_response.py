"""Generated from Smithy shape ``com.amazonaws.pinpoint#SendOTPMessageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.message_response


class SendOTPMessageResponse(TypedDict, closed=True):
    message_response: NotRequired[
        "capo_pinpoint.types.message_response.MessageResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: SendOTPMessageResponse) -> dict:
    out: dict = {}
    if "message_response" in value:
        import capo_pinpoint.types.message_response

        out["MessageResponse"] = capo_pinpoint.types.message_response.serialize_json(
            value["message_response"]
        )
    return out


def deserialize_json(data: dict) -> SendOTPMessageResponse:
    out: SendOTPMessageResponse = {}  # type: ignore[typeddict-item]
    if "MessageResponse" in data:
        import capo_pinpoint.types.message_response

        out["message_response"] = capo_pinpoint.types.message_response.deserialize_json(
            data["MessageResponse"]
        )
    return out
