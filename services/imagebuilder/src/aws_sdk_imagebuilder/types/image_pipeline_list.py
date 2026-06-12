"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImagePipelineList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.image_pipeline

ImagePipelineList: TypeAlias = list[
    "aws_sdk_imagebuilder.types.image_pipeline.ImagePipeline"
]


# --- restJson1 ser/de ---
def serialize_json(value: ImagePipelineList) -> list:
    import aws_sdk_imagebuilder.types.image_pipeline

    out: list = []
    for item in value:
        out.append(aws_sdk_imagebuilder.types.image_pipeline.serialize_json(item))
    return out


def deserialize_json(data: list) -> ImagePipelineList:
    import aws_sdk_imagebuilder.types.image_pipeline

    out: ImagePipelineList = []
    for item in data:
        out.append(aws_sdk_imagebuilder.types.image_pipeline.deserialize_json(item))
    return out
