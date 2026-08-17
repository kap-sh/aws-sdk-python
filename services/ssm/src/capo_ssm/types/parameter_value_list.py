"""Generated from Smithy shape ``com.amazonaws.ssm#ParameterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.parameter_value

ParameterValueList: TypeAlias = list["capo_ssm.types.parameter_value.ParameterValue"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterValueList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ParameterValueList:
    return [item for item in data if item is not None]
