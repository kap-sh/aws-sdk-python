"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetEmailChannelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.email_channel_response


class GetEmailChannelResponse(TypedDict, closed=True):
    email_channel_response: NotRequired[
        "aws_sdk_pinpoint.types.email_channel_response.EmailChannelResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetEmailChannelResponse) -> dict:
    out: dict = {}
    if "email_channel_response" in value:
        import aws_sdk_pinpoint.types.email_channel_response

        out["EmailChannelResponse"] = (
            aws_sdk_pinpoint.types.email_channel_response.serialize_json(
                value["email_channel_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetEmailChannelResponse:
    out: GetEmailChannelResponse = {}  # type: ignore[typeddict-item]
    if "EmailChannelResponse" in data:
        import aws_sdk_pinpoint.types.email_channel_response

        out["email_channel_response"] = (
            aws_sdk_pinpoint.types.email_channel_response.deserialize_json(
                data["EmailChannelResponse"]
            )
        )
    return out
