"""Generated from Smithy shape ``com.amazonaws.medialive#StandardHlsSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string
    import capo_medialive.types.m3u8_settings


class StandardHlsSettings(TypedDict, closed=True):
    audio_rendition_sets: NotRequired["capo_medialive.types.__string.__string"]
    """List all the audio groups that are used with the video output stream. Input all the audio GROUP-IDs that are associated to the video, separate by ','."""
    m3u8_settings: NotRequired["capo_medialive.types.m3u8_settings.M3u8Settings"]


# --- restJson1 ser/de ---
def serialize_json(value: StandardHlsSettings) -> dict:
    out: dict = {}
    if "audio_rendition_sets" in value:
        out["audioRenditionSets"] = value["audio_rendition_sets"]
    if "m3u8_settings" in value:
        import capo_medialive.types.m3u8_settings

        out["m3u8Settings"] = capo_medialive.types.m3u8_settings.serialize_json(
            value["m3u8_settings"]
        )
    return out


def deserialize_json(data: dict) -> StandardHlsSettings:
    out: StandardHlsSettings = {}  # type: ignore[typeddict-item]
    if "audioRenditionSets" in data:
        out["audio_rendition_sets"] = data["audioRenditionSets"]
    if "m3u8Settings" in data:
        import capo_medialive.types.m3u8_settings

        out["m3u8_settings"] = capo_medialive.types.m3u8_settings.deserialize_json(
            data["m3u8Settings"]
        )
    return out
