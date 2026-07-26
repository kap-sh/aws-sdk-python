"""Generated from Smithy shape ``com.amazonaws.athena#ExecutionParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_athena.types.execution_parameter

ExecutionParameters: TypeAlias = list[
    "capo_athena.types.execution_parameter.ExecutionParameter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionParameters) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ExecutionParameters:
    return list(data)
