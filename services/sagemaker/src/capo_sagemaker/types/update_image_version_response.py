"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateImageVersionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.image_version_arn


class UpdateImageVersionResponse(TypedDict, closed=True):
    image_version_arn: NotRequired[
        "capo_sagemaker.types.image_version_arn.ImageVersionArn"
    ]
    """<p>The ARN of the image version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateImageVersionResponse) -> dict:
    out: dict = {}
    if "image_version_arn" in value:
        out["ImageVersionArn"] = value["image_version_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateImageVersionResponse:
    out: UpdateImageVersionResponse = {}  # type: ignore[typeddict-item]
    if "ImageVersionArn" in data:
        out["image_version_arn"] = data["ImageVersionArn"]
    return out
