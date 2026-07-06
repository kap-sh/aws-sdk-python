"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetApnsVoipChannelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.apns_voip_channel_response


class GetApnsVoipChannelResponse(TypedDict, closed=True):
    apns_voip_channel_response: NotRequired[
        "aws_sdk_pinpoint.types.apns_voip_channel_response.APNSVoipChannelResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetApnsVoipChannelResponse) -> dict:
    out: dict = {}
    if "apns_voip_channel_response" in value:
        import aws_sdk_pinpoint.types.apns_voip_channel_response

        out["APNSVoipChannelResponse"] = (
            aws_sdk_pinpoint.types.apns_voip_channel_response.serialize_json(
                value["apns_voip_channel_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetApnsVoipChannelResponse:
    out: GetApnsVoipChannelResponse = {}  # type: ignore[typeddict-item]
    if "APNSVoipChannelResponse" in data:
        import aws_sdk_pinpoint.types.apns_voip_channel_response

        out["apns_voip_channel_response"] = (
            aws_sdk_pinpoint.types.apns_voip_channel_response.deserialize_json(
                data["APNSVoipChannelResponse"]
            )
        )
    return out
