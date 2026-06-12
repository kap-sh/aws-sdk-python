"""Generated from Smithy shape ``com.amazonaws.medialive#Smpte2110ReceiverGroupSdpSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_input_sdp_location
    import aws_sdk_medialive.types.input_sdp_location


class Smpte2110ReceiverGroupSdpSettings(TypedDict):
    ancillary_sdps: NotRequired[
        "aws_sdk_medialive.types.__list_of_input_sdp_location.__listOfInputSdpLocation"
    ]
    """A list of InputSdpLocations. Each item in the list specifies the SDP file and index for one ancillary SMPTE 2110 stream. Each stream encapsulates one captions stream (out of any number you can include) or the single SCTE 35 stream that you can include."""
    audio_sdps: NotRequired[
        "aws_sdk_medialive.types.__list_of_input_sdp_location.__listOfInputSdpLocation"
    ]
    """A list of InputSdpLocations. Each item in the list specifies the SDP file and index for one audio SMPTE 2110 stream."""
    video_sdp: NotRequired[
        "aws_sdk_medialive.types.input_sdp_location.InputSdpLocation"
    ]
    """The InputSdpLocation that specifies the SDP file and index for the single video SMPTE 2110 stream for this 2110 input."""


# --- restJson1 ser/de ---
def serialize_json(value: Smpte2110ReceiverGroupSdpSettings) -> dict:
    out: dict = {}
    if "ancillary_sdps" in value:
        import aws_sdk_medialive.types.__list_of_input_sdp_location

        out["ancillarySdps"] = (
            aws_sdk_medialive.types.__list_of_input_sdp_location.serialize_json(
                value["ancillary_sdps"]
            )
        )
    if "audio_sdps" in value:
        import aws_sdk_medialive.types.__list_of_input_sdp_location

        out["audioSdps"] = (
            aws_sdk_medialive.types.__list_of_input_sdp_location.serialize_json(
                value["audio_sdps"]
            )
        )
    if "video_sdp" in value:
        import aws_sdk_medialive.types.input_sdp_location

        out["videoSdp"] = aws_sdk_medialive.types.input_sdp_location.serialize_json(
            value["video_sdp"]
        )
    return out


def deserialize_json(data: dict) -> Smpte2110ReceiverGroupSdpSettings:
    out: Smpte2110ReceiverGroupSdpSettings = {}  # type: ignore[typeddict-item]
    if "ancillarySdps" in data:
        import aws_sdk_medialive.types.__list_of_input_sdp_location

        out["ancillary_sdps"] = (
            aws_sdk_medialive.types.__list_of_input_sdp_location.deserialize_json(
                data["ancillarySdps"]
            )
        )
    if "audioSdps" in data:
        import aws_sdk_medialive.types.__list_of_input_sdp_location

        out["audio_sdps"] = (
            aws_sdk_medialive.types.__list_of_input_sdp_location.deserialize_json(
                data["audioSdps"]
            )
        )
    if "videoSdp" in data:
        import aws_sdk_medialive.types.input_sdp_location

        out["video_sdp"] = aws_sdk_medialive.types.input_sdp_location.deserialize_json(
            data["videoSdp"]
        )
    return out
