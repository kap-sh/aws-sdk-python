"""Generated from Smithy shape ``com.amazonaws.braket#ProgramSetValidationFailuresList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_braket.types.program_set_validation_failure

ProgramSetValidationFailuresList: TypeAlias = list[
    "capo_braket.types.program_set_validation_failure.ProgramSetValidationFailure"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProgramSetValidationFailuresList) -> list:
    import capo_braket.types.program_set_validation_failure

    out: list = []
    for item in value:
        out.append(
            capo_braket.types.program_set_validation_failure.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ProgramSetValidationFailuresList:
    import capo_braket.types.program_set_validation_failure

    out: ProgramSetValidationFailuresList = []
    for item in data:
        out.append(
            capo_braket.types.program_set_validation_failure.deserialize_json(item)
        )
    return out
