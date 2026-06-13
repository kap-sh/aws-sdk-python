"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#StepOutputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.step_output

StepOutputList: TypeAlias = list[
    "aws_sdk_migrationhuborchestrator.types.step_output.StepOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: StepOutputList) -> list:
    import aws_sdk_migrationhuborchestrator.types.step_output

    out: list = []
    for item in value:
        out.append(
            aws_sdk_migrationhuborchestrator.types.step_output.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> StepOutputList:
    import aws_sdk_migrationhuborchestrator.types.step_output

    out: StepOutputList = []
    for item in data:
        out.append(
            aws_sdk_migrationhuborchestrator.types.step_output.deserialize_json(item)
        )
    return out
