"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateImageResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.image_arn


class UpdateImageResponse(TypedDict):
    image_arn: NotRequired["aws_sdk_sagemaker.types.image_arn.ImageArn"]
    """<p>The ARN of the image.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateImageResponse) -> dict:
    out: dict = {}
    if "image_arn" in value:
        out["ImageArn"] = value["image_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateImageResponse:
    out: UpdateImageResponse = {}  # type: ignore[typeddict-item]
    if "ImageArn" in data:
        out["image_arn"] = data["ImageArn"]
    return out
