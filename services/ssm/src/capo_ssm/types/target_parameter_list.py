"""Generated from Smithy shape ``com.amazonaws.ssm#TargetParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.parameter_value

TargetParameterList: TypeAlias = list["capo_ssm.types.parameter_value.ParameterValue"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetParameterList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> TargetParameterList:
    return [item for item in data if item is not None]
