"""Generated from Smithy shape ``com.amazonaws.imagebuilder#DeleteImagePipelineRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.image_pipeline_arn


class DeleteImagePipelineRequest(TypedDict):
    image_pipeline_arn: "aws_sdk_imagebuilder.types.image_pipeline_arn.ImagePipelineArn"
    """<p>The Amazon Resource Name (ARN) of the image pipeline to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteImagePipelineRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteImagePipelineRequest:
    out: DeleteImagePipelineRequest = {}  # type: ignore[typeddict-item]
    return out
