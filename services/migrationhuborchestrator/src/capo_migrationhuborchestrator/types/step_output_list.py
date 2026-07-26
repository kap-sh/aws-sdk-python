"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#StepOutputList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.step_output

StepOutputList: TypeAlias = list[
    "capo_migrationhuborchestrator.types.step_output.StepOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: StepOutputList) -> list:
    import capo_migrationhuborchestrator.types.step_output

    out: list = []
    for item in value:
        out.append(capo_migrationhuborchestrator.types.step_output.serialize_json(item))
    return out


def deserialize_json(data: list) -> StepOutputList:
    import capo_migrationhuborchestrator.types.step_output

    out: StepOutputList = []
    for item in data:
        out.append(
            capo_migrationhuborchestrator.types.step_output.deserialize_json(item)
        )
    return out
