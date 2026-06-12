"""Generated from Smithy shape ``com.amazonaws.emr#EbsBlockDeviceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr.types.ebs_block_device

EbsBlockDeviceList: TypeAlias = list[
    "aws_sdk_emr.types.ebs_block_device.EbsBlockDevice"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EbsBlockDeviceList) -> list:
    import aws_sdk_emr.types.ebs_block_device

    out: list = []
    for item in value:
        out.append(aws_sdk_emr.types.ebs_block_device.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EbsBlockDeviceList:
    import aws_sdk_emr.types.ebs_block_device

    out: EbsBlockDeviceList = []
    for item in data:
        out.append(aws_sdk_emr.types.ebs_block_device.deserialize_aws_json_1_1(item))
    return out
