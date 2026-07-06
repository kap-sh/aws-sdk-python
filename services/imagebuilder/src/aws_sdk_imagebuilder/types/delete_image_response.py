"""Generated from Smithy shape ``com.amazonaws.imagebuilder#DeleteImageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.image_build_version_arn
    import aws_sdk_imagebuilder.types.non_empty_string


class DeleteImageResponse(TypedDict, closed=True):
    request_id: NotRequired[
        "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
    ]
    """<p>The request ID that uniquely identifies this request.</p>"""
    image_build_version_arn: NotRequired[
        "aws_sdk_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the Image Builder image resource that this request deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteImageResponse) -> dict:
    out: dict = {}
    if "request_id" in value:
        out["requestId"] = value["request_id"]
    if "image_build_version_arn" in value:
        out["imageBuildVersionArn"] = value["image_build_version_arn"]
    return out


def deserialize_json(data: dict) -> DeleteImageResponse:
    out: DeleteImageResponse = {}  # type: ignore[typeddict-item]
    if "requestId" in data:
        out["request_id"] = data["requestId"]
    if "imageBuildVersionArn" in data:
        out["image_build_version_arn"] = data["imageBuildVersionArn"]
    return out
