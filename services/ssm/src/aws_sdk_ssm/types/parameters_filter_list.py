"""Generated from Smithy shape ``com.amazonaws.ssm#ParametersFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.parameters_filter

ParametersFilterList: TypeAlias = list[
    "aws_sdk_ssm.types.parameters_filter.ParametersFilter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParametersFilterList) -> list:
    import aws_sdk_ssm.types.parameters_filter

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.parameters_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ParametersFilterList:
    import aws_sdk_ssm.types.parameters_filter

    out: ParametersFilterList = []
    for item in data:
        out.append(aws_sdk_ssm.types.parameters_filter.deserialize_aws_json_1_1(item))
    return out
