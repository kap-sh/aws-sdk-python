"""Generated from Smithy shape ``com.amazonaws.emr#EbsVolumeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr.types.ebs_volume

EbsVolumeList: TypeAlias = list["aws_sdk_emr.types.ebs_volume.EbsVolume"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EbsVolumeList) -> list:
    import aws_sdk_emr.types.ebs_volume

    out: list = []
    for item in value:
        out.append(aws_sdk_emr.types.ebs_volume.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EbsVolumeList:
    import aws_sdk_emr.types.ebs_volume

    out: EbsVolumeList = []
    for item in data:
        out.append(aws_sdk_emr.types.ebs_volume.deserialize_aws_json_1_1(item))
    return out
