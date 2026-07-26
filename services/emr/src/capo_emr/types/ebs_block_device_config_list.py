"""Generated from Smithy shape ``com.amazonaws.emr#EbsBlockDeviceConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_emr.types.ebs_block_device_config

EbsBlockDeviceConfigList: TypeAlias = list[
    "capo_emr.types.ebs_block_device_config.EbsBlockDeviceConfig"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EbsBlockDeviceConfigList) -> list:
    import capo_emr.types.ebs_block_device_config

    out: list = []
    for item in value:
        out.append(capo_emr.types.ebs_block_device_config.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EbsBlockDeviceConfigList:
    import capo_emr.types.ebs_block_device_config

    out: EbsBlockDeviceConfigList = []
    for item in data:
        out.append(
            capo_emr.types.ebs_block_device_config.deserialize_aws_json_1_1(item)
        )
    return out
