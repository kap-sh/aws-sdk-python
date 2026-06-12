"""Generated from Smithy shape ``com.amazonaws.imagebuilder#GetImageRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.image_version_arn_or_build_version_arn


class GetImageRequest(TypedDict):
    image_build_version_arn: "aws_sdk_imagebuilder.types.image_version_arn_or_build_version_arn.ImageVersionArnOrBuildVersionArn"
    """<p>The Amazon Resource Name (ARN) of the image that you want to get.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetImageRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetImageRequest:
    out: GetImageRequest = {}  # type: ignore[typeddict-item]
    return out
