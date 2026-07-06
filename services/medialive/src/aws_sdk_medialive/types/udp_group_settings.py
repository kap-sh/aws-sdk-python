"""Generated from Smithy shape ``com.amazonaws.medialive#UdpGroupSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__integer_min0
    import aws_sdk_medialive.types.input_loss_action_for_udp_out
    import aws_sdk_medialive.types.udp_timed_metadata_id3_frame


class UdpGroupSettings(TypedDict, closed=True):
    input_loss_action: NotRequired[
        "aws_sdk_medialive.types.input_loss_action_for_udp_out.InputLossActionForUdpOut"
    ]
    """Specifies behavior of last resort when input video is lost, and no more backup inputs are available. When dropTs is selected the entire transport stream will stop being emitted. When dropProgram is selected the program can be dropped from the transport stream (and replaced with null packets to meet the TS bitrate requirement). Or, when emitProgram is chosen the transport stream will continue to be produced normally with repeat frames, black frames, or slate frames substituted for the absent input video."""
    timed_metadata_id3_frame: NotRequired[
        "aws_sdk_medialive.types.udp_timed_metadata_id3_frame.UdpTimedMetadataId3Frame"
    ]
    """Indicates ID3 frame that has the timecode."""
    timed_metadata_id3_period: NotRequired[
        "aws_sdk_medialive.types.__integer_min0.__integerMin0"
    ]
    """Timed Metadata interval in seconds."""


# --- restJson1 ser/de ---
def serialize_json(value: UdpGroupSettings) -> dict:
    out: dict = {}
    if "input_loss_action" in value:
        import aws_sdk_medialive.types.input_loss_action_for_udp_out

        out["inputLossAction"] = (
            aws_sdk_medialive.types.input_loss_action_for_udp_out.serialize_json(
                value["input_loss_action"]
            )
        )
    if "timed_metadata_id3_frame" in value:
        import aws_sdk_medialive.types.udp_timed_metadata_id3_frame

        out["timedMetadataId3Frame"] = (
            aws_sdk_medialive.types.udp_timed_metadata_id3_frame.serialize_json(
                value["timed_metadata_id3_frame"]
            )
        )
    if "timed_metadata_id3_period" in value:
        out["timedMetadataId3Period"] = value["timed_metadata_id3_period"]
    return out


def deserialize_json(data: dict) -> UdpGroupSettings:
    out: UdpGroupSettings = {}  # type: ignore[typeddict-item]
    if "inputLossAction" in data:
        import aws_sdk_medialive.types.input_loss_action_for_udp_out

        out["input_loss_action"] = (
            aws_sdk_medialive.types.input_loss_action_for_udp_out.deserialize_json(
                data["inputLossAction"]
            )
        )
    if "timedMetadataId3Frame" in data:
        import aws_sdk_medialive.types.udp_timed_metadata_id3_frame

        out["timed_metadata_id3_frame"] = (
            aws_sdk_medialive.types.udp_timed_metadata_id3_frame.deserialize_json(
                data["timedMetadataId3Frame"]
            )
        )
    if "timedMetadataId3Period" in data:
        out["timed_metadata_id3_period"] = data["timedMetadataId3Period"]
    return out
