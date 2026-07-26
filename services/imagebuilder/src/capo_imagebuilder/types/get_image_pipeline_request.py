"""Generated from Smithy shape ``com.amazonaws.imagebuilder#GetImagePipelineRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.image_pipeline_arn


class GetImagePipelineRequest(TypedDict, closed=True):
    image_pipeline_arn: "capo_imagebuilder.types.image_pipeline_arn.ImagePipelineArn"
    """<p>The Amazon Resource Name (ARN) of the image pipeline that you want to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetImagePipelineRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetImagePipelineRequest:
    out: GetImagePipelineRequest = {}  # type: ignore[typeddict-item]
    return out
