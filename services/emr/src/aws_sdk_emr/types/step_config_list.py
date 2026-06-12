"""Generated from Smithy shape ``com.amazonaws.emr#StepConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr.types.step_config

StepConfigList: TypeAlias = list["aws_sdk_emr.types.step_config.StepConfig"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StepConfigList) -> list:
    import aws_sdk_emr.types.step_config

    out: list = []
    for item in value:
        out.append(aws_sdk_emr.types.step_config.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> StepConfigList:
    import aws_sdk_emr.types.step_config

    out: StepConfigList = []
    for item in data:
        out.append(aws_sdk_emr.types.step_config.deserialize_aws_json_1_1(item))
    return out
