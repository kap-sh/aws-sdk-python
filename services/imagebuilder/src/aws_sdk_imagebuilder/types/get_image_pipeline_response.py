"""Generated from Smithy shape ``com.amazonaws.imagebuilder#GetImagePipelineResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.image_pipeline
    import aws_sdk_imagebuilder.types.non_empty_string


class GetImagePipelineResponse(TypedDict):
    request_id: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The request ID that uniquely identifies this request.</p>"""
    image_pipeline: NotRequired[
        "aws_sdk_imagebuilder.types.image_pipeline.ImagePipeline"
    ]
    """<p>The image pipeline object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetImagePipelineResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "image_pipeline" in value:
        import aws_sdk_imagebuilder.types.image_pipeline

        out["imagePipeline"] = aws_sdk_imagebuilder.types.image_pipeline.serialize_json(
            value["image_pipeline"]
        )
    return out


def deserialize_json(data: dict) -> GetImagePipelineResponse:
    out: GetImagePipelineResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "imagePipeline" in data:
        import aws_sdk_imagebuilder.types.image_pipeline

        out["image_pipeline"] = (
            aws_sdk_imagebuilder.types.image_pipeline.deserialize_json(
                data["imagePipeline"]
            )
        )
    return out
