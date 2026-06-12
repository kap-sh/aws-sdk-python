"""Generated from Smithy shape ``com.amazonaws.chimesdkmediapipelines#ConcatenationSource``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_chime_sdk_media_pipelines.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime_sdk_media_pipelines.types.concatenation_source_type
    import aws_sdk_chime_sdk_media_pipelines.types.media_capture_pipeline_source_configuration


class ConcatenationSource(TypedDict):
    type: "aws_sdk_chime_sdk_media_pipelines.types.concatenation_source_type.ConcatenationSourceType"
    """<p>The type of concatenation source in a configuration object.</p>"""
    media_capture_pipeline_source_configuration: "aws_sdk_chime_sdk_media_pipelines.types.media_capture_pipeline_source_configuration.MediaCapturePipelineSourceConfiguration"
    """<p>The concatenation settings for the media pipeline in a configuration object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConcatenationSource) -> dict:
    out: dict = {}
    import aws_sdk_chime_sdk_media_pipelines.types.concatenation_source_type

    out["Type"] = (
        aws_sdk_chime_sdk_media_pipelines.types.concatenation_source_type.serialize_json(
            value["type"]
        )
    )
    import aws_sdk_chime_sdk_media_pipelines.types.media_capture_pipeline_source_configuration

    out["MediaCapturePipelineSourceConfiguration"] = (
        aws_sdk_chime_sdk_media_pipelines.types.media_capture_pipeline_source_configuration.serialize_json(
            value["media_capture_pipeline_source_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> ConcatenationSource:
    out: ConcatenationSource = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.concatenation_source_type

        out["type"] = (
            aws_sdk_chime_sdk_media_pipelines.types.concatenation_source_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("ConcatenationSource.type required")
    if "MediaCapturePipelineSourceConfiguration" in data:
        import aws_sdk_chime_sdk_media_pipelines.types.media_capture_pipeline_source_configuration

        out["media_capture_pipeline_source_configuration"] = (
            aws_sdk_chime_sdk_media_pipelines.types.media_capture_pipeline_source_configuration.deserialize_json(
                data["MediaCapturePipelineSourceConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "ConcatenationSource.media_capture_pipeline_source_configuration required"
        )
    return out
