"""Generated from Smithy shape ``com.amazonaws.medialive#Smpte2110ReceiverGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.smpte2110_receiver_group_sdp_settings


class Smpte2110ReceiverGroup(TypedDict, closed=True):
    sdp_settings: NotRequired[
        "capo_medialive.types.smpte2110_receiver_group_sdp_settings.Smpte2110ReceiverGroupSdpSettings"
    ]
    """The single Smpte2110ReceiverGroupSdpSettings that identify the video, audio, and ancillary streams for this receiver group."""


# --- restJson1 ser/de ---
def serialize_json(value: Smpte2110ReceiverGroup) -> dict:
    out: dict = {}
    if "sdp_settings" in value:
        import capo_medialive.types.smpte2110_receiver_group_sdp_settings

        out["sdpSettings"] = (
            capo_medialive.types.smpte2110_receiver_group_sdp_settings.serialize_json(
                value["sdp_settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> Smpte2110ReceiverGroup:
    out: Smpte2110ReceiverGroup = {}  # type: ignore[typeddict-item]
    if "sdpSettings" in data:
        import capo_medialive.types.smpte2110_receiver_group_sdp_settings

        out["sdp_settings"] = (
            capo_medialive.types.smpte2110_receiver_group_sdp_settings.deserialize_json(
                data["sdpSettings"]
            )
        )
    return out
