"""Generated from Smithy shape ``com.amazonaws.imagebuilder#GetImagePolicyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.image_build_version_arn


class GetImagePolicyRequest(TypedDict, closed=True):
    image_arn: "aws_sdk_imagebuilder.types.image_build_version_arn.ImageBuildVersionArn"
    """<p>The Amazon Resource Name (ARN) of the image whose policy you want to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetImagePolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetImagePolicyRequest:
    out: GetImagePolicyRequest = {}  # type: ignore[typeddict-item]
    return out
