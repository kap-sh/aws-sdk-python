"""Generated from Smithy shape ``com.amazonaws.sagemaker#CustomImage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.app_image_config_name
    import aws_sdk_sagemaker.types.image_name
    import aws_sdk_sagemaker.types.image_version_number


class CustomImage(TypedDict):
    image_name: NotRequired["aws_sdk_sagemaker.types.image_name.ImageName"]
    """<p>The name of the CustomImage. Must be unique to your account.</p>"""
    image_version_number: NotRequired[
        "aws_sdk_sagemaker.types.image_version_number.ImageVersionNumber"
    ]
    """<p>The version number of the CustomImage.</p>"""
    app_image_config_name: NotRequired[
        "aws_sdk_sagemaker.types.app_image_config_name.AppImageConfigName"
    ]
    """<p>The name of the AppImageConfig.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomImage) -> dict:
    out: dict = {}
    if "image_name" in value:
        out["ImageName"] = value["image_name"]
    if "image_version_number" in value:
        out["ImageVersionNumber"] = value["image_version_number"]
    if "app_image_config_name" in value:
        out["AppImageConfigName"] = value["app_image_config_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomImage:
    out: CustomImage = {}  # type: ignore[typeddict-item]
    if "ImageName" in data:
        out["image_name"] = data["ImageName"]
    if "ImageVersionNumber" in data:
        out["image_version_number"] = data["ImageVersionNumber"]
    if "AppImageConfigName" in data:
        out["app_image_config_name"] = data["AppImageConfigName"]
    return out
