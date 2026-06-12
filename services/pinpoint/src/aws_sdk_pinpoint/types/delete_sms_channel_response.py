"""Generated from Smithy shape ``com.amazonaws.pinpoint#DeleteSmsChannelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.sms_channel_response


class DeleteSmsChannelResponse(TypedDict):
    sms_channel_response: NotRequired[
        "aws_sdk_pinpoint.types.sms_channel_response.SMSChannelResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteSmsChannelResponse) -> dict:
    out: dict = {}
    if "sms_channel_response" in value:
        import aws_sdk_pinpoint.types.sms_channel_response

        out["SMSChannelResponse"] = (
            aws_sdk_pinpoint.types.sms_channel_response.serialize_json(
                value["sms_channel_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteSmsChannelResponse:
    out: DeleteSmsChannelResponse = {}  # type: ignore[typeddict-item]
    if "SMSChannelResponse" in data:
        import aws_sdk_pinpoint.types.sms_channel_response

        out["sms_channel_response"] = (
            aws_sdk_pinpoint.types.sms_channel_response.deserialize_json(
                data["SMSChannelResponse"]
            )
        )
    return out
