"""Generated from Smithy shape ``com.amazonaws.ssm#ParameterLabelList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm.types.parameter_label

ParameterLabelList: TypeAlias = list["aws_sdk_ssm.types.parameter_label.ParameterLabel"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ParameterLabelList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ParameterLabelList:
    return list(data)
