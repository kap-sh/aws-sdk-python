"""Generated from Smithy shape ``com.amazonaws.pinpoint#UpdateApnsVoipChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.apns_voip_channel_request


class UpdateApnsVoipChannelRequest(TypedDict, closed=True):
    apns_voip_channel_request: NotRequired[
        "capo_pinpoint.types.apns_voip_channel_request.APNSVoipChannelRequest"
    ]
    application_id: "capo_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApnsVoipChannelRequest) -> dict:
    out: dict = {}
    if "apns_voip_channel_request" in value:
        import capo_pinpoint.types.apns_voip_channel_request

        out["APNSVoipChannelRequest"] = (
            capo_pinpoint.types.apns_voip_channel_request.serialize_json(
                value["apns_voip_channel_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateApnsVoipChannelRequest:
    out: UpdateApnsVoipChannelRequest = {}  # type: ignore[typeddict-item]
    if "APNSVoipChannelRequest" in data:
        import capo_pinpoint.types.apns_voip_channel_request

        out["apns_voip_channel_request"] = (
            capo_pinpoint.types.apns_voip_channel_request.deserialize_json(
                data["APNSVoipChannelRequest"]
            )
        )
    return out
