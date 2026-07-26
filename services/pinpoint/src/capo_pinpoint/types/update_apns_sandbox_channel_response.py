"""Generated from Smithy shape ``com.amazonaws.pinpoint#UpdateApnsSandboxChannelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.apns_sandbox_channel_response


class UpdateApnsSandboxChannelResponse(TypedDict, closed=True):
    apns_sandbox_channel_response: NotRequired[
        "capo_pinpoint.types.apns_sandbox_channel_response.APNSSandboxChannelResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateApnsSandboxChannelResponse) -> dict:
    out: dict = {}
    if "apns_sandbox_channel_response" in value:
        import capo_pinpoint.types.apns_sandbox_channel_response

        out["APNSSandboxChannelResponse"] = (
            capo_pinpoint.types.apns_sandbox_channel_response.serialize_json(
                value["apns_sandbox_channel_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateApnsSandboxChannelResponse:
    out: UpdateApnsSandboxChannelResponse = {}  # type: ignore[typeddict-item]
    if "APNSSandboxChannelResponse" in data:
        import capo_pinpoint.types.apns_sandbox_channel_response

        out["apns_sandbox_channel_response"] = (
            capo_pinpoint.types.apns_sandbox_channel_response.deserialize_json(
                data["APNSSandboxChannelResponse"]
            )
        )
    return out
