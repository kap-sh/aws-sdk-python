"""Generated from Smithy shape ``com.amazonaws.frauddetector#EventVariableMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.variable_name
    import aws_sdk_frauddetector.types.variable_value

EventVariableMap: TypeAlias = dict[
    "aws_sdk_frauddetector.types.variable_name.variableName",
    "aws_sdk_frauddetector.types.variable_value.variableValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: EventVariableMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> EventVariableMap:
    out: EventVariableMap = {}
    for key, value in data.items():
        out[key] = value
    return out
