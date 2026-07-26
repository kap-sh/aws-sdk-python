"""Generated from Smithy shape ``com.amazonaws.ivs#IngestConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.audio_configuration
    import capo_ivs.types.video_configuration


class IngestConfiguration(TypedDict, closed=True):
    video: NotRequired["capo_ivs.types.video_configuration.VideoConfiguration"]
    """<p>Encoder settings for video.</p>"""
    audio: NotRequired["capo_ivs.types.audio_configuration.AudioConfiguration"]
    """<p>Encoder settings for audio.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IngestConfiguration) -> dict:
    out: dict = {}
    if "video" in value:
        import capo_ivs.types.video_configuration

        out["video"] = capo_ivs.types.video_configuration.serialize_json(value["video"])
    if "audio" in value:
        import capo_ivs.types.audio_configuration

        out["audio"] = capo_ivs.types.audio_configuration.serialize_json(value["audio"])
    return out


def deserialize_json(data: dict) -> IngestConfiguration:
    out: IngestConfiguration = {}  # type: ignore[typeddict-item]
    if "video" in data:
        import capo_ivs.types.video_configuration

        out["video"] = capo_ivs.types.video_configuration.deserialize_json(
            data["video"]
        )
    if "audio" in data:
        import capo_ivs.types.audio_configuration

        out["audio"] = capo_ivs.types.audio_configuration.deserialize_json(
            data["audio"]
        )
    return out
