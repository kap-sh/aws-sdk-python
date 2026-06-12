"""Generated from Smithy shape ``com.amazonaws.ssm#ParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.parameter

ParameterList: TypeAlias = list["aws_sdk_ssm.types.parameter.Parameter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterList) -> list:
    import aws_sdk_ssm.types.parameter

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm.types.parameter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ParameterList:
    import aws_sdk_ssm.types.parameter

    out: ParameterList = []
    for item in data:
        out.append(aws_sdk_ssm.types.parameter.deserialize_aws_json_1_1(item))
    return out
