"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ExecutionResult``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.execution_result_key
    import aws_sdk_iotsitewise.types.execution_result_value

ExecutionResult: TypeAlias = dict[
    "aws_sdk_iotsitewise.types.execution_result_key.ExecutionResultKey",
    "aws_sdk_iotsitewise.types.execution_result_value.ExecutionResultValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ExecutionResult) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ExecutionResult:
    out: ExecutionResult = {}
    for key, value in data.items():
        out[key] = value
    return out
