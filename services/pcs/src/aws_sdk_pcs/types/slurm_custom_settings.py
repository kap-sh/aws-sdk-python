"""Generated from Smithy shape ``com.amazonaws.pcs#SlurmCustomSettings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pcs.types.slurm_custom_setting

SlurmCustomSettings: TypeAlias = list[
    "aws_sdk_pcs.types.slurm_custom_setting.SlurmCustomSetting"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SlurmCustomSettings) -> list:
    import aws_sdk_pcs.types.slurm_custom_setting

    out: list = []
    for item in value:
        out.append(aws_sdk_pcs.types.slurm_custom_setting.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> SlurmCustomSettings:
    import aws_sdk_pcs.types.slurm_custom_setting

    out: SlurmCustomSettings = []
    for item in data:
        out.append(
            aws_sdk_pcs.types.slurm_custom_setting.deserialize_aws_json_1_0(item)
        )
    return out
