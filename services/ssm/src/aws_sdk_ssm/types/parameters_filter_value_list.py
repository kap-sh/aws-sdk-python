"""Generated from Smithy shape ``com.amazonaws.ssm#ParametersFilterValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.parameters_filter_value

ParametersFilterValueList: TypeAlias = list[
    "aws_sdk_ssm.types.parameters_filter_value.ParametersFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParametersFilterValueList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ParametersFilterValueList:
    return list(data)
