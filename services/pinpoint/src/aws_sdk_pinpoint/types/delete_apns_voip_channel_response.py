"""Generated from Smithy shape ``com.amazonaws.pinpoint#DeleteApnsVoipChannelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.apns_voip_channel_response


class DeleteApnsVoipChannelResponse(TypedDict):
    apns_voip_channel_response: NotRequired[
        "aws_sdk_pinpoint.types.apns_voip_channel_response.APNSVoipChannelResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteApnsVoipChannelResponse) -> dict:
    out: dict = {}
    if "apns_voip_channel_response" in value:
        import aws_sdk_pinpoint.types.apns_voip_channel_response

        out["APNSVoipChannelResponse"] = (
            aws_sdk_pinpoint.types.apns_voip_channel_response.serialize_json(
                value["apns_voip_channel_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteApnsVoipChannelResponse:
    out: DeleteApnsVoipChannelResponse = {}  # type: ignore[typeddict-item]
    if "APNSVoipChannelResponse" in data:
        import aws_sdk_pinpoint.types.apns_voip_channel_response

        out["apns_voip_channel_response"] = (
            aws_sdk_pinpoint.types.apns_voip_channel_response.deserialize_json(
                data["APNSVoipChannelResponse"]
            )
        )
    return out
