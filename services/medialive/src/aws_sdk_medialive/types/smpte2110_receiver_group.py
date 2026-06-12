"""Generated from Smithy shape ``com.amazonaws.medialive#Smpte2110ReceiverGroup``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.smpte2110_receiver_group_sdp_settings


class Smpte2110ReceiverGroup(TypedDict):
    sdp_settings: NotRequired[
        "aws_sdk_medialive.types.smpte2110_receiver_group_sdp_settings.Smpte2110ReceiverGroupSdpSettings"
    ]
    """The single Smpte2110ReceiverGroupSdpSettings that identify the video, audio, and ancillary streams for this receiver group."""


# --- restJson1 ser/de ---
def serialize_json(value: Smpte2110ReceiverGroup) -> dict:
    out: dict = {}
    if "sdp_settings" in value:
        import aws_sdk_medialive.types.smpte2110_receiver_group_sdp_settings

        out["sdpSettings"] = (
            aws_sdk_medialive.types.smpte2110_receiver_group_sdp_settings.serialize_json(
                value["sdp_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> Smpte2110ReceiverGroup:
    out: Smpte2110ReceiverGroup = {}  # type: ignore[typeddict-item]
    if "sdpSettings" in data:
        import aws_sdk_medialive.types.smpte2110_receiver_group_sdp_settings

        out["sdp_settings"] = (
            aws_sdk_medialive.types.smpte2110_receiver_group_sdp_settings.deserialize_json(
                data["sdpSettings"]
            )
        )
    return out
