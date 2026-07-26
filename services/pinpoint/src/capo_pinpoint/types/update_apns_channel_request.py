"""Generated from Smithy shape ``com.amazonaws.pinpoint#UpdateApnsChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.apns_channel_request


class UpdateApnsChannelRequest(TypedDict, closed=True):
    apns_channel_request: NotRequired[
        "capo_pinpoint.types.apns_channel_request.APNSChannelRequest"
    ]
    application_id: "capo_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApnsChannelRequest) -> dict:
    out: dict = {}
    if "apns_channel_request" in value:
        import capo_pinpoint.types.apns_channel_request

        out["APNSChannelRequest"] = (
            capo_pinpoint.types.apns_channel_request.serialize_json(
                value["apns_channel_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateApnsChannelRequest:
    out: UpdateApnsChannelRequest = {}  # type: ignore[typeddict-item]
    if "APNSChannelRequest" in data:
        import capo_pinpoint.types.apns_channel_request

        out["apns_channel_request"] = (
            capo_pinpoint.types.apns_channel_request.deserialize_json(
                data["APNSChannelRequest"]
            )
        )
    return out
