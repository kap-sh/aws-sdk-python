"""Generated from Smithy shape ``com.amazonaws.pinpoint#DeleteApnsSandboxChannelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.apns_sandbox_channel_response


class DeleteApnsSandboxChannelResponse(TypedDict, closed=True):
    apns_sandbox_channel_response: NotRequired[
        "capo_pinpoint.types.apns_sandbox_channel_response.APNSSandboxChannelResponse"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteApnsSandboxChannelResponse) -> dict:
    out: dict = {}
    if "apns_sandbox_channel_response" in value:
        import capo_pinpoint.types.apns_sandbox_channel_response

        out["APNSSandboxChannelResponse"] = (
            capo_pinpoint.types.apns_sandbox_channel_response.serialize_json(
                value["apns_sandbox_channel_response"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteApnsSandboxChannelResponse:
    out: DeleteApnsSandboxChannelResponse = {}  # type: ignore[typeddict-item]
    if "APNSSandboxChannelResponse" in data:
        import capo_pinpoint.types.apns_sandbox_channel_response

        out["apns_sandbox_channel_response"] = (
            capo_pinpoint.types.apns_sandbox_channel_response.deserialize_json(
                data["APNSSandboxChannelResponse"]
            )
        )
    return out
