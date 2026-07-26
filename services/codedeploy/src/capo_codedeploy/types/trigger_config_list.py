"""Generated from Smithy shape ``com.amazonaws.codedeploy#TriggerConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codedeploy.types.trigger_config

TriggerConfigList: TypeAlias = list[
    "capo_codedeploy.types.trigger_config.TriggerConfig"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TriggerConfigList) -> list:
    import capo_codedeploy.types.trigger_config

    out: list = []
    for item in value:
        out.append(capo_codedeploy.types.trigger_config.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> TriggerConfigList:
    import capo_codedeploy.types.trigger_config

    out: TriggerConfigList = []
    for item in data:
        out.append(capo_codedeploy.types.trigger_config.deserialize_aws_json_1_1(item))
    return out
