"""Generated from Smithy shape ``com.amazonaws.emr#BootstrapActionConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr.types.bootstrap_action_config

BootstrapActionConfigList: TypeAlias = list[
    "aws_sdk_emr.types.bootstrap_action_config.BootstrapActionConfig"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BootstrapActionConfigList) -> list:
    import aws_sdk_emr.types.bootstrap_action_config

    out: list = []
    for item in value:
        out.append(
            aws_sdk_emr.types.bootstrap_action_config.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BootstrapActionConfigList:
    import aws_sdk_emr.types.bootstrap_action_config

    out: BootstrapActionConfigList = []
    for item in data:
        out.append(
            aws_sdk_emr.types.bootstrap_action_config.deserialize_aws_json_1_1(item)
        )
    return out
