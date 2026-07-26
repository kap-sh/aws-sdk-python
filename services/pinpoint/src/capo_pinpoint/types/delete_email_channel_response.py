"""Generated from Smithy shape ``com.amazonaws.pinpoint#DeleteEmailChannelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.email_channel_response


class DeleteEmailChannelResponse(TypedDict, closed=True):
    email_channel_response: NotRequired[
        "capo_pinpoint.types.email_channel_response.EmailChannelResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEmailChannelResponse) -> dict:
    out: dict = {}
    if "email_channel_response" in value:
        import capo_pinpoint.types.email_channel_response

        out["EmailChannelResponse"] = (
            capo_pinpoint.types.email_channel_response.serialize_json(
                value["email_channel_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteEmailChannelResponse:
    out: DeleteEmailChannelResponse = {}  # type: ignore[typeddict-item]
    if "EmailChannelResponse" in data:
        import capo_pinpoint.types.email_channel_response

        out["email_channel_response"] = (
            capo_pinpoint.types.email_channel_response.deserialize_json(
                data["EmailChannelResponse"]
            )
        )
    return out
