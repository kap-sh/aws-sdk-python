"""Generated from Smithy shape ``com.amazonaws.pinpoint#UpdateApnsSandboxChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.apns_sandbox_channel_request


class UpdateApnsSandboxChannelRequest(TypedDict, closed=True):
    apns_sandbox_channel_request: NotRequired[
        "aws_sdk_pinpoint.types.apns_sandbox_channel_request.APNSSandboxChannelRequest"
    ]
    application_id: "aws_sdk_pinpoint.types.__string.__string"
    """<p>The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApnsSandboxChannelRequest) -> dict:
    out: dict = {}
    if "apns_sandbox_channel_request" in value:
        import aws_sdk_pinpoint.types.apns_sandbox_channel_request

        out["APNSSandboxChannelRequest"] = (
            aws_sdk_pinpoint.types.apns_sandbox_channel_request.serialize_json(
                value["apns_sandbox_channel_request"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateApnsSandboxChannelRequest:
    out: UpdateApnsSandboxChannelRequest = {}  # type: ignore[typeddict-item]
    if "APNSSandboxChannelRequest" in data:
        import aws_sdk_pinpoint.types.apns_sandbox_channel_request

        out["apns_sandbox_channel_request"] = (
            aws_sdk_pinpoint.types.apns_sandbox_channel_request.deserialize_json(
                data["APNSSandboxChannelRequest"]
            )
        )
    return out
