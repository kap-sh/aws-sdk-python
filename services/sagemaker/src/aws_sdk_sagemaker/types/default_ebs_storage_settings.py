"""Generated from Smithy shape ``com.amazonaws.sagemaker#DefaultEbsStorageSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.space_ebs_volume_size_in_gb


class DefaultEbsStorageSettings(TypedDict, closed=True):
    default_ebs_volume_size_in_gb: NotRequired[
        "aws_sdk_sagemaker.types.space_ebs_volume_size_in_gb.SpaceEbsVolumeSizeInGb"
    ]
    """<p>The default size of the EBS storage volume for a space.</p>"""
    maximum_ebs_volume_size_in_gb: NotRequired[
        "aws_sdk_sagemaker.types.space_ebs_volume_size_in_gb.SpaceEbsVolumeSizeInGb"
    ]
    """<p>The maximum size of the EBS storage volume for a space.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DefaultEbsStorageSettings) -> dict:
    out: dict = {}
    if "default_ebs_volume_size_in_gb" in value:
        out["DefaultEbsVolumeSizeInGb"] = value["default_ebs_volume_size_in_gb"]
    if "maximum_ebs_volume_size_in_gb" in value:
        out["MaximumEbsVolumeSizeInGb"] = value["maximum_ebs_volume_size_in_gb"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DefaultEbsStorageSettings:
    out: DefaultEbsStorageSettings = {}  # type: ignore[typeddict-item]
    if "DefaultEbsVolumeSizeInGb" in data:
        out["default_ebs_volume_size_in_gb"] = data["DefaultEbsVolumeSizeInGb"]
    if "MaximumEbsVolumeSizeInGb" in data:
        out["maximum_ebs_volume_size_in_gb"] = data["MaximumEbsVolumeSizeInGb"]
    return out
