"""Generated from Smithy shape ``com.amazonaws.sagemaker#EbsStorageSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.space_ebs_volume_size_in_gb


class EbsStorageSettings(TypedDict, closed=True):
    ebs_volume_size_in_gb: NotRequired[
        "aws_sdk_sagemaker.types.space_ebs_volume_size_in_gb.SpaceEbsVolumeSizeInGb"
    ]
    """<p>The size of an EBS storage volume for a space.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EbsStorageSettings) -> dict:
    out: dict = {}
    if "ebs_volume_size_in_gb" in value:
        out["EbsVolumeSizeInGb"] = value["ebs_volume_size_in_gb"]
    return out


def deserialize_aws_json_1_1(data: dict) -> EbsStorageSettings:
    out: EbsStorageSettings = {}  # type: ignore[typeddict-item]
    if "EbsVolumeSizeInGb" in data:
        out["ebs_volume_size_in_gb"] = data["EbsVolumeSizeInGb"]
    return out
