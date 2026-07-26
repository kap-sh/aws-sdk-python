"""Generated from Smithy shape ``com.amazonaws.pinpoint#UpdateGcmChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.gcm_channel_request


class UpdateGcmChannelRequest(TypedDict, closed=True):
    application_id: "capo_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    gcm_channel_request: NotRequired[
        "capo_pinpoint.types.gcm_channel_request.GCMChannelRequest"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGcmChannelRequest) -> dict:
    out: dict = {}
    if "gcm_channel_request" in value:
        import capo_pinpoint.types.gcm_channel_request

        out["GCMChannelRequest"] = (
            capo_pinpoint.types.gcm_channel_request.serialize_json(
                value["gcm_channel_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateGcmChannelRequest:
    out: UpdateGcmChannelRequest = {}  # type: ignore[typeddict-item]
    if "GCMChannelRequest" in data:
        import capo_pinpoint.types.gcm_channel_request

        out["gcm_channel_request"] = (
            capo_pinpoint.types.gcm_channel_request.deserialize_json(
                data["GCMChannelRequest"]
            )
        )
    return out
