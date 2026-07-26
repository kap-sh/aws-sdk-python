"""Generated from Smithy shape ``com.amazonaws.pinpoint#DeleteGcmChannelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.gcm_channel_response


class DeleteGcmChannelResponse(TypedDict, closed=True):
    gcm_channel_response: NotRequired[
        "capo_pinpoint.types.gcm_channel_response.GCMChannelResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGcmChannelResponse) -> dict:
    out: dict = {}
    if "gcm_channel_response" in value:
        import capo_pinpoint.types.gcm_channel_response

        out["GCMChannelResponse"] = (
            capo_pinpoint.types.gcm_channel_response.serialize_json(
                value["gcm_channel_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteGcmChannelResponse:
    out: DeleteGcmChannelResponse = {}  # type: ignore[typeddict-item]
    if "GCMChannelResponse" in data:
        import capo_pinpoint.types.gcm_channel_response

        out["gcm_channel_response"] = (
            capo_pinpoint.types.gcm_channel_response.deserialize_json(
                data["GCMChannelResponse"]
            )
        )
    return out
