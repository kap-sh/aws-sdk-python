"""Generated from Smithy shape ``com.amazonaws.pinpoint#DeleteGcmChannelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.gcm_channel_response


class DeleteGcmChannelResponse(TypedDict):
    gcm_channel_response: NotRequired[
        "aws_sdk_pinpoint.types.gcm_channel_response.GCMChannelResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGcmChannelResponse) -> dict:
    out: dict = {}
    if "gcm_channel_response" in value:
        import aws_sdk_pinpoint.types.gcm_channel_response

        out["GCMChannelResponse"] = (
            aws_sdk_pinpoint.types.gcm_channel_response.serialize_json(
                value["gcm_channel_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteGcmChannelResponse:
    out: DeleteGcmChannelResponse = {}  # type: ignore[typeddict-item]
    if "GCMChannelResponse" in data:
        import aws_sdk_pinpoint.types.gcm_channel_response

        out["gcm_channel_response"] = (
            aws_sdk_pinpoint.types.gcm_channel_response.deserialize_json(
                data["GCMChannelResponse"]
            )
        )
    return out
