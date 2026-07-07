"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeImageVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.image_name
    import aws_sdk_sagemaker.types.image_version_number
    import aws_sdk_sagemaker.types.sage_maker_image_version_alias


class DescribeImageVersionRequest(TypedDict, closed=True):
    image_name: NotRequired["aws_sdk_sagemaker.types.image_name.ImageName"]
    """<p>The name of the image.</p>"""
    version: NotRequired[
        "aws_sdk_sagemaker.types.image_version_number.ImageVersionNumber"
    ]
    """<p>The version of the image. If not specified, the latest version is described.</p>"""
    alias: NotRequired[
        "aws_sdk_sagemaker.types.sage_maker_image_version_alias.SageMakerImageVersionAlias"
    ]
    """<p>The alias of the image version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeImageVersionRequest) -> dict:
    out: dict = {}
    if "image_name" in value:
        out["ImageName"] = value["image_name"]
    if "version" in value:
        out["Version"] = value["version"]
    if "alias" in value:
        out["Alias"] = value["alias"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeImageVersionRequest:
    out: DescribeImageVersionRequest = {}  # type: ignore[typeddict-item]
    if "ImageName" in data:
        out["image_name"] = data["ImageName"]
    if "Version" in data:
        out["version"] = data["Version"]
    if "Alias" in data:
        out["alias"] = data["Alias"]
    return out
