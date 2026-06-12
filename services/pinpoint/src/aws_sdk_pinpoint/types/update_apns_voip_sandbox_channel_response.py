"""Generated from Smithy shape ``com.amazonaws.pinpoint#UpdateApnsVoipSandboxChannelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.apns_voip_sandbox_channel_response


class UpdateApnsVoipSandboxChannelResponse(TypedDict):
    apns_voip_sandbox_channel_response: NotRequired[
        "aws_sdk_pinpoint.types.apns_voip_sandbox_channel_response.APNSVoipSandboxChannelResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApnsVoipSandboxChannelResponse) -> dict:
    out: dict = {}
    if "apns_voip_sandbox_channel_response" in value:
        import aws_sdk_pinpoint.types.apns_voip_sandbox_channel_response

        out["APNSVoipSandboxChannelResponse"] = (
            aws_sdk_pinpoint.types.apns_voip_sandbox_channel_response.serialize_json(
                value["apns_voip_sandbox_channel_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateApnsVoipSandboxChannelResponse:
    out: UpdateApnsVoipSandboxChannelResponse = {}  # type: ignore[typeddict-item]
    if "APNSVoipSandboxChannelResponse" in data:
        import aws_sdk_pinpoint.types.apns_voip_sandbox_channel_response

        out["apns_voip_sandbox_channel_response"] = (
            aws_sdk_pinpoint.types.apns_voip_sandbox_channel_response.deserialize_json(
                data["APNSVoipSandboxChannelResponse"]
            )
        )
    return out
