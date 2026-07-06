"""Generated from Smithy shape ``com.amazonaws.imagebuilder#PutImagePolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.image_build_version_arn
    import aws_sdk_imagebuilder.types.non_empty_string


class PutImagePolicyResponse(TypedDict, closed=True):
    request_id: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The request ID that uniquely identifies this request.</p>"""
    image_arn: NotRequired[
        "aws_sdk_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the image that this policy was applied to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutImagePolicyResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "image_arn" in value:
        out["imageArn"] = value["image_arn"]
    return out


def deserialize_json(data: dict) -> PutImagePolicyResponse:
    out: PutImagePolicyResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "imageArn" in data:
        out["image_arn"] = data["imageArn"]
    return out
