"""Generated from Smithy shape ``com.amazonaws.pinpoint#DeleteApnsVoipChannelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.apns_voip_channel_response


class DeleteApnsVoipChannelResponse(TypedDict, closed=True):
    apns_voip_channel_response: NotRequired[
        "capo_pinpoint.types.apns_voip_channel_response.APNSVoipChannelResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteApnsVoipChannelResponse) -> dict:
    out: dict = {}
    if "apns_voip_channel_response" in value:
        import capo_pinpoint.types.apns_voip_channel_response

        out["APNSVoipChannelResponse"] = (
            capo_pinpoint.types.apns_voip_channel_response.serialize_json(
                value["apns_voip_channel_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteApnsVoipChannelResponse:
    out: DeleteApnsVoipChannelResponse = {}  # type: ignore[typeddict-item]
    if "APNSVoipChannelResponse" in data:
        import capo_pinpoint.types.apns_voip_channel_response

        out["apns_voip_channel_response"] = (
            capo_pinpoint.types.apns_voip_channel_response.deserialize_json(
                data["APNSVoipChannelResponse"]
            )
        )
    return out
