"""Generated from Smithy shape ``com.amazonaws.sfn#AssignedVariables``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sfn.types.variable_name
    import aws_sdk_sfn.types.variable_value

AssignedVariables: TypeAlias = dict[
    "aws_sdk_sfn.types.variable_name.VariableName",
    "aws_sdk_sfn.types.variable_value.VariableValue",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: AssignedVariables) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_0(data: dict) -> AssignedVariables:
    out: AssignedVariables = {}
    for key, value in data.items():
        out[key] = value
    return out
