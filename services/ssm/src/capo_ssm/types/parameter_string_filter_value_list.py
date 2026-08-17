"""Generated from Smithy shape ``com.amazonaws.ssm#ParameterStringFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ssm.types.parameter_string_filter_value

ParameterStringFilterValueList: TypeAlias = list[
    "capo_ssm.types.parameter_string_filter_value.ParameterStringFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterStringFilterValueList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ParameterStringFilterValueList:
    return [item for item in data if item is not None]
