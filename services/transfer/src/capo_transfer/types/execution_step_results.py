"""Generated from Smithy shape ``com.amazonaws.transfer#ExecutionStepResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transfer.types.execution_step_result

ExecutionStepResults: TypeAlias = list[
    "capo_transfer.types.execution_step_result.ExecutionStepResult"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionStepResults) -> list:
    import capo_transfer.types.execution_step_result

    out: list = []
    for item in value:
        out.append(
            capo_transfer.types.execution_step_result.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ExecutionStepResults:
    import capo_transfer.types.execution_step_result

    out: ExecutionStepResults = []
    for item in data:
        out.append(
            capo_transfer.types.execution_step_result.deserialize_aws_json_1_1(item)
        )
    return out
