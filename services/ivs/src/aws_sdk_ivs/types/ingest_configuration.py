"""Generated from Smithy shape ``com.amazonaws.ivs#IngestConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ivs.types.audio_configuration
    import aws_sdk_ivs.types.video_configuration


class IngestConfiguration(TypedDict):
    video: NotRequired["aws_sdk_ivs.types.video_configuration.VideoConfiguration"]
    """<p>Encoder settings for video.</p>"""
    audio: NotRequired["aws_sdk_ivs.types.audio_configuration.AudioConfiguration"]
    """<p>Encoder settings for audio.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IngestConfiguration) -> dict:
    out: dict = {}
    if "video" in value:
        import aws_sdk_ivs.types.video_configuration

        out["video"] = aws_sdk_ivs.types.video_configuration.serialize_json(
            value["video"]
        )
    if "audio" in value:
        import aws_sdk_ivs.types.audio_configuration

        out["audio"] = aws_sdk_ivs.types.audio_configuration.serialize_json(
            value["audio"]
        )
    return out


def deserialize_json(data: dict) -> IngestConfiguration:
    out: IngestConfiguration = {}  # type: ignore[typeddict-item]
    if "video" in data:
        import aws_sdk_ivs.types.video_configuration

        out["video"] = aws_sdk_ivs.types.video_configuration.deserialize_json(
            data["video"]
        )
    if "audio" in data:
        import aws_sdk_ivs.types.audio_configuration

        out["audio"] = aws_sdk_ivs.types.audio_configuration.deserialize_json(
            data["audio"]
        )
    return out
