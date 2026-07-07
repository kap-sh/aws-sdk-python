"""Generated from Smithy shape ``com.amazonaws.medialive#AudioTrackSelection``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__list_of_audio_track
    import aws_sdk_medialive.types.audio_dolby_e_decode


class AudioTrackSelection(TypedDict, closed=True):
    tracks: NotRequired[
        "aws_sdk_medialive.types.__list_of_audio_track.__listOfAudioTrack"
    ]
    """Selects one or more unique audio tracks from within a source."""
    dolby_e_decode: NotRequired[
        "aws_sdk_medialive.types.audio_dolby_e_decode.AudioDolbyEDecode"
    ]
    """Configure decoding options for Dolby E streams - these should be Dolby E frames carried in PCM streams tagged with SMPTE-337"""


# --- restJson1 ser/de ---
def serialize_json(value: AudioTrackSelection) -> dict:
    out: dict = {}
    if "tracks" in value:
        import aws_sdk_medialive.types.__list_of_audio_track

        out["tracks"] = aws_sdk_medialive.types.__list_of_audio_track.serialize_json(
            value["tracks"]
        )
    if "dolby_e_decode" in value:
        import aws_sdk_medialive.types.audio_dolby_e_decode

        out["dolbyEDecode"] = (
            aws_sdk_medialive.types.audio_dolby_e_decode.serialize_json(
                value["dolby_e_decode"]
            )
        )
    return out


def deserialize_json(data: dict) -> AudioTrackSelection:
    out: AudioTrackSelection = {}  # type: ignore[typeddict-item]
    if "tracks" in data:
        import aws_sdk_medialive.types.__list_of_audio_track

        out["tracks"] = aws_sdk_medialive.types.__list_of_audio_track.deserialize_json(
            data["tracks"]
        )
    if "dolbyEDecode" in data:
        import aws_sdk_medialive.types.audio_dolby_e_decode

        out["dolby_e_decode"] = (
            aws_sdk_medialive.types.audio_dolby_e_decode.deserialize_json(
                data["dolbyEDecode"]
            )
        )
    return out
