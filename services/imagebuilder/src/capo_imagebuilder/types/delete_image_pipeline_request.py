"""Generated from Smithy shape ``com.amazonaws.imagebuilder#DeleteImagePipelineRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.image_pipeline_arn


class DeleteImagePipelineRequest(TypedDict, closed=True):
    image_pipeline_arn: "capo_imagebuilder.types.image_pipeline_arn.ImagePipelineArn"
    """<p>The Amazon Resource Name (ARN) of the image pipeline to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteImagePipelineRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteImagePipelineRequest:
    out: DeleteImagePipelineRequest = {}  # type: ignore[typeddict-item]
    return out
