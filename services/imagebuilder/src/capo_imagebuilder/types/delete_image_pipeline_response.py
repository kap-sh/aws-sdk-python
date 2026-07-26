"""Generated from Smithy shape ``com.amazonaws.imagebuilder#DeleteImagePipelineResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.image_pipeline_arn
    import capo_imagebuilder.types.non_empty_string


class DeleteImagePipelineResponse(TypedDict, closed=True):
    request_id: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The request ID that uniquely identifies this request.</p>"""
    image_pipeline_arn: NotRequired[
        "capo_imagebuilder.types.image_pipeline_arn.ImagePipelineArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the image pipeline that was deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteImagePipelineResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "image_pipeline_arn" in value:
        out["imagePipelineArn"] = value["image_pipeline_arn"]
    return out


def deserialize_json(data: dict) -> DeleteImagePipelineResponse:
    out: DeleteImagePipelineResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "imagePipelineArn" in data:
        out["image_pipeline_arn"] = data["imagePipelineArn"]
    return out
