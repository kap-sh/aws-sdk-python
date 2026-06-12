"""Generated from Smithy shape ``com.amazonaws.pinpoint#GetApnsSandboxChannelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.apns_sandbox_channel_response


class GetApnsSandboxChannelResponse(TypedDict):
    apns_sandbox_channel_response: NotRequired[
        "aws_sdk_pinpoint.types.apns_sandbox_channel_response.APNSSandboxChannelResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: GetApnsSandboxChannelResponse) -> dict:
    out: dict = {}
    if "apns_sandbox_channel_response" in value:
        import aws_sdk_pinpoint.types.apns_sandbox_channel_response

        out["APNSSandboxChannelResponse"] = (
            aws_sdk_pinpoint.types.apns_sandbox_channel_response.serialize_json(
                value["apns_sandbox_channel_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetApnsSandboxChannelResponse:
    out: GetApnsSandboxChannelResponse = {}  # type: ignore[typeddict-item]
    if "APNSSandboxChannelResponse" in data:
        import aws_sdk_pinpoint.types.apns_sandbox_channel_response

        out["apns_sandbox_channel_response"] = (
            aws_sdk_pinpoint.types.apns_sandbox_channel_response.deserialize_json(
                data["APNSSandboxChannelResponse"]
            )
        )
    return out
