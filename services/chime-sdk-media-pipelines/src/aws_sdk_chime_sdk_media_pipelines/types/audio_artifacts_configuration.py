"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#AudioArtifactsConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.audio_mux_type


class AudioArtifactsConfiguration(TypedDict, closed=True):
    mux_type: "aws_sdk_chime_sdk_media_pipelines.types.audio_mux_type.AudioMuxType"
    """<p>The MUX type of the audio artifact configuration object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudioArtifactsConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_chime_sdk_media_pipelines.types.audio_mux_type

    out["MuxType"] = (
        aws_sdk_chime_sdk_media_pipelines.types.audio_mux_type.serialize_json(
            value["mux_type"]
        )
    )
    return out


def deserialize_json(data: dict) -> AudioArtifactsConfiguration:
    out: AudioArtifactsConfiguration = {}  # type: ignore[typeddict-item]
    if "MuxType" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.audio_mux_type

        out["mux_type"] = (
            aws_sdk_chime_sdk_media_pipelines.types.audio_mux_type.deserialize_json(
                data["MuxType"]
            )
        )
    else:
        raise DeserializationError("AudioArtifactsConfiguration.mux_type required")
    return out
