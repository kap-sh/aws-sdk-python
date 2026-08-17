"""Generated from Smithy shape ``com.amazonaws.ssm#ParameterNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.ps_parameter_name

ParameterNameList: TypeAlias = list["capo_ssm.types.ps_parameter_name.PSParameterName"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterNameList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ParameterNameList:
    return [item for item in data if item is not None]
