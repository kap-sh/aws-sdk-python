"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetApnsChannelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.apns_channel_response


class GetApnsChannelResponse(TypedDict, closed=True):
    apns_channel_response: NotRequired[
        "capo_pinpoint.types.apns_channel_response.APNSChannelResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetApnsChannelResponse) -> dict:
    out: dict = {}
    if "apns_channel_response" in value:
        import capo_pinpoint.types.apns_channel_response

        out["APNSChannelResponse"] = (
            capo_pinpoint.types.apns_channel_response.serialize_json(
                value["apns_channel_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetApnsChannelResponse:
    out: GetApnsChannelResponse = {}  # type: ignore[typeddict-item]
    if "APNSChannelResponse" in data:
        import capo_pinpoint.types.apns_channel_response

        out["apns_channel_response"] = (
            capo_pinpoint.types.apns_channel_response.deserialize_json(
                data["APNSChannelResponse"]
            )
        )
    return out
