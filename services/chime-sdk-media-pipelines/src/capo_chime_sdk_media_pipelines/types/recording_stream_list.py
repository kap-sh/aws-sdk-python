"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#RecordingStreamList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_media_pipelines.types.recording_stream_configuration

RecordingStreamList: TypeAlias = list[
    "capo_chime_sdk_media_pipelines.types.recording_stream_configuration.RecordingStreamConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecordingStreamList) -> list:
    import capo_chime_sdk_media_pipelines.types.recording_stream_configuration

    out: list = []
    for item in value:
        out.append(
            capo_chime_sdk_media_pipelines.types.recording_stream_configuration.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> RecordingStreamList:
    import capo_chime_sdk_media_pipelines.types.recording_stream_configuration

    out: RecordingStreamList = []
    for item in data:
        out.append(
            capo_chime_sdk_media_pipelines.types.recording_stream_configuration.deserialize_json(
                item
            )
        )
    return out
