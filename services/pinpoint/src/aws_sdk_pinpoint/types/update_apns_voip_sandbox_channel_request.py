"""Generated from Smithy shape ``com.amazonaws.pinpoint#UpdateApnsVoipSandboxChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.apns_voip_sandbox_channel_request


class UpdateApnsVoipSandboxChannelRequest(TypedDict, closed=True):
    apns_voip_sandbox_channel_request: NotRequired[
        "aws_sdk_pinpoint.types.apns_voip_sandbox_channel_request.APNSVoipSandboxChannelRequest"
    ]
    application_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApnsVoipSandboxChannelRequest) -> dict:
    out: dict = {}
    if "apns_voip_sandbox_channel_request" in value:
        import aws_sdk_pinpoint.types.apns_voip_sandbox_channel_request

        out["APNSVoipSandboxChannelRequest"] = (
            aws_sdk_pinpoint.types.apns_voip_sandbox_channel_request.serialize_json(
                value["apns_voip_sandbox_channel_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateApnsVoipSandboxChannelRequest:
    out: UpdateApnsVoipSandboxChannelRequest = {}  # type: ignore[typeddict-item]
    if "APNSVoipSandboxChannelRequest" in data:
        import aws_sdk_pinpoint.types.apns_voip_sandbox_channel_request

        out["apns_voip_sandbox_channel_request"] = (
            aws_sdk_pinpoint.types.apns_voip_sandbox_channel_request.deserialize_json(
                data["APNSVoipSandboxChannelRequest"]
            )
        )
    return out
