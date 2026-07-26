"""Generated from Smithy shape ``com.amazonaws.pinpoint#UpdateSmsChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.sms_channel_request


class UpdateSmsChannelRequest(TypedDict, closed=True):
    application_id: "capo_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    sms_channel_request: NotRequired[
        "capo_pinpoint.types.sms_channel_request.SMSChannelRequest"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSmsChannelRequest) -> dict:
    out: dict = {}
    if "sms_channel_request" in value:
        import capo_pinpoint.types.sms_channel_request

        out["SMSChannelRequest"] = (
            capo_pinpoint.types.sms_channel_request.serialize_json(
                value["sms_channel_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateSmsChannelRequest:
    out: UpdateSmsChannelRequest = {}  # type: ignore[typeddict-item]
    if "SMSChannelRequest" in data:
        import capo_pinpoint.types.sms_channel_request

        out["sms_channel_request"] = (
            capo_pinpoint.types.sms_channel_request.deserialize_json(
                data["SMSChannelRequest"]
            )
        )
    return out
