"""Generated from Smithy shape ``com.amazonaws.frauddetector#VariableList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.variable

VariableList: TypeAlias = list["aws_sdk_frauddetector.types.variable.Variable"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VariableList) -> list:
    import aws_sdk_frauddetector.types.variable

    out: list = []
    for item in value:
        out.append(aws_sdk_frauddetector.types.variable.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> VariableList:
    import aws_sdk_frauddetector.types.variable

    out: VariableList = []
    for item in data:
        out.append(aws_sdk_frauddetector.types.variable.deserialize_aws_json_1_1(item))
    return out
