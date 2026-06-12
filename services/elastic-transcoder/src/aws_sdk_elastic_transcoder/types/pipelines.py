"""Generated from Smithy shape ``com.amazonaws.elastictranscoder#Pipelines``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_elastic_transcoder.types.pipeline

Pipelines: TypeAlias = list["aws_sdk_elastic_transcoder.types.pipeline.Pipeline"]


# --- restJson1 ser/de ---
def serialize_json(value: Pipelines) -> list:
    import aws_sdk_elastic_transcoder.types.pipeline

    out: list = []
    for item in value:
        out.append(aws_sdk_elastic_transcoder.types.pipeline.serialize_json(item))
    return out


def deserialize_json(data: list) -> Pipelines:
    import aws_sdk_elastic_transcoder.types.pipeline

    out: Pipelines = []
    for item in data:
        out.append(aws_sdk_elastic_transcoder.types.pipeline.deserialize_json(item))
    return out
