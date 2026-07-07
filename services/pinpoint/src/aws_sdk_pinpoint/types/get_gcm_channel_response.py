"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetGcmChannelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.gcm_channel_response


class GetGcmChannelResponse(TypedDict, closed=True):
    gcm_channel_response: NotRequired[
        "aws_sdk_pinpoint.types.gcm_channel_response.GCMChannelResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetGcmChannelResponse) -> dict:
    out: dict = {}
    if "gcm_channel_response" in value:
        import aws_sdk_pinpoint.types.gcm_channel_response

        out["GCMChannelResponse"] = (
            aws_sdk_pinpoint.types.gcm_channel_response.serialize_json(
                value["gcm_channel_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetGcmChannelResponse:
    out: GetGcmChannelResponse = {}  # type: ignore[typeddict-item]
    if "GCMChannelResponse" in data:
        import aws_sdk_pinpoint.types.gcm_channel_response

        out["gcm_channel_response"] = (
            aws_sdk_pinpoint.types.gcm_channel_response.deserialize_json(
                data["GCMChannelResponse"]
            )
        )
    return out
