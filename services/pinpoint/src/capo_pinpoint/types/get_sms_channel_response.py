"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetSmsChannelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.sms_channel_response


class GetSmsChannelResponse(TypedDict, closed=True):
    sms_channel_response: NotRequired[
        "capo_pinpoint.types.sms_channel_response.SMSChannelResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetSmsChannelResponse) -> dict:
    out: dict = {}
    if "sms_channel_response" in value:
        import capo_pinpoint.types.sms_channel_response

        out["SMSChannelResponse"] = (
            capo_pinpoint.types.sms_channel_response.serialize_json(
                value["sms_channel_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetSmsChannelResponse:
    out: GetSmsChannelResponse = {}  # type: ignore[typeddict-item]
    if "SMSChannelResponse" in data:
        import capo_pinpoint.types.sms_channel_response

        out["sms_channel_response"] = (
            capo_pinpoint.types.sms_channel_response.deserialize_json(
                data["SMSChannelResponse"]
            )
        )
    return out
