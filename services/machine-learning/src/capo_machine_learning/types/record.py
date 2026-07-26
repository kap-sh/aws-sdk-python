"""Generated from Smithy shape ``com.amazonaws.machinelearning#Record``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_machine_learning.types.variable_name
    import capo_machine_learning.types.variable_value

Record: TypeAlias = dict[
    "capo_machine_learning.types.variable_name.VariableName",
    "capo_machine_learning.types.variable_value.VariableValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: Record) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> Record:
    out: Record = {}
    for key, value in data.items():
        out[key] = value
    return out
