"""Generated from Smithy shape ``com.amazonaws.pinpoint#UpdateSmsChannelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.sms_channel_response


class UpdateSmsChannelResponse(TypedDict, closed=True):
    sms_channel_response: NotRequired[
        "aws_sdk_pinpoint.types.sms_channel_response.SMSChannelResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSmsChannelResponse) -> dict:
    out: dict = {}
    if "sms_channel_response" in value:
        import aws_sdk_pinpoint.types.sms_channel_response

        out["SMSChannelResponse"] = (
            aws_sdk_pinpoint.types.sms_channel_response.serialize_json(
                value["sms_channel_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateSmsChannelResponse:
    out: UpdateSmsChannelResponse = {}  # type: ignore[typeddict-item]
    if "SMSChannelResponse" in data:
        import aws_sdk_pinpoint.types.sms_channel_response

        out["sms_channel_response"] = (
            aws_sdk_pinpoint.types.sms_channel_response.deserialize_json(
                data["SMSChannelResponse"]
            )
        )
    return out
