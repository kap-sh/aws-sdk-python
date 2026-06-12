"""Generated from Smithy shape ``com.amazonaws.pinpoint#DeleteApnsChannelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.apns_channel_response


class DeleteApnsChannelResponse(TypedDict):
    apns_channel_response: NotRequired[
        "aws_sdk_pinpoint.types.apns_channel_response.APNSChannelResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteApnsChannelResponse) -> dict:
    out: dict = {}
    if "apns_channel_response" in value:
        import aws_sdk_pinpoint.types.apns_channel_response

        out["APNSChannelResponse"] = (
            aws_sdk_pinpoint.types.apns_channel_response.serialize_json(
                value["apns_channel_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteApnsChannelResponse:
    out: DeleteApnsChannelResponse = {}  # type: ignore[typeddict-item]
    if "APNSChannelResponse" in data:
        import aws_sdk_pinpoint.types.apns_channel_response

        out["apns_channel_response"] = (
            aws_sdk_pinpoint.types.apns_channel_response.deserialize_json(
                data["APNSChannelResponse"]
            )
        )
    return out
