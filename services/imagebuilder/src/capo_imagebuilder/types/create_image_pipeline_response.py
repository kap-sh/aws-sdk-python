"""Generated from Smithy shape ``com.amazonaws.imagebuilder#CreateImagePipelineResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_imagebuilder.types.client_token
    import capo_imagebuilder.types.image_pipeline_arn
    import capo_imagebuilder.types.non_empty_string


class CreateImagePipelineResponse(TypedDict, closed=True):
    request_id: NotRequired["capo_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>The request ID that uniquely identifies this request.</p>"""
    client_token: NotRequired["capo_imagebuilder.types.client_token.ClientToken"]
    """<p>The client token that uniquely identifies the request.</p>"""
    image_pipeline_arn: NotRequired[
        "capo_imagebuilder.types.image_pipeline_arn.ImagePipelineArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the image pipeline that was created by this request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateImagePipelineResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "image_pipeline_arn" in value:
        out["imagePipelineArn"] = value["image_pipeline_arn"]
    return out


def deserialize_json(data: dict) -> CreateImagePipelineResponse:
    out: CreateImagePipelineResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "imagePipelineArn" in data:
        out["image_pipeline_arn"] = data["imagePipelineArn"]
    return out
