"""Generated from Smithy shape ``com.amazonaws.pcs#SlurmdbdCustomSettings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_pcs.types.slurmdbd_custom_setting

SlurmdbdCustomSettings: TypeAlias = list[
    "aws_sdk_pcs.types.slurmdbd_custom_setting.SlurmdbdCustomSetting"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SlurmdbdCustomSettings) -> list:
    import aws_sdk_pcs.types.slurmdbd_custom_setting

    out: list = []
    for item in value:
        out.append(
            aws_sdk_pcs.types.slurmdbd_custom_setting.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> SlurmdbdCustomSettings:
    import aws_sdk_pcs.types.slurmdbd_custom_setting

    out: SlurmdbdCustomSettings = []
    for item in data:
        out.append(
            aws_sdk_pcs.types.slurmdbd_custom_setting.deserialize_aws_json_1_0(item)
        )
    return out
