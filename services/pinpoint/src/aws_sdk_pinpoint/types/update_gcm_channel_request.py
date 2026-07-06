"""Generated from Smithy shape ``com.amazonaws.pinpoint#UpdateGcmChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.gcm_channel_request


class UpdateGcmChannelRequest(TypedDict, closed=True):
    application_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""
    gcm_channel_request: NotRequired[
        "aws_sdk_pinpoint.types.gcm_channel_request.GCMChannelRequest"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGcmChannelRequest) -> dict:
    out: dict = {}
    if "gcm_channel_request" in value:
        import aws_sdk_pinpoint.types.gcm_channel_request

        out["GCMChannelRequest"] = (
            aws_sdk_pinpoint.types.gcm_channel_request.serialize_json(
                value["gcm_channel_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateGcmChannelRequest:
    out: UpdateGcmChannelRequest = {}  # type: ignore[typeddict-item]
    if "GCMChannelRequest" in data:
        import aws_sdk_pinpoint.types.gcm_channel_request

        out["gcm_channel_request"] = (
            aws_sdk_pinpoint.types.gcm_channel_request.deserialize_json(
                data["GCMChannelRequest"]
            )
        )
    return out
