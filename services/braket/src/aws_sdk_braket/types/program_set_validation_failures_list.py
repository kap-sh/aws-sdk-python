"""Generated from Smithy shape ``com.amazonaws.braket#ProgramSetValidationFailuresList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_braket.types.program_set_validation_failure

ProgramSetValidationFailuresList: TypeAlias = list[
    "aws_sdk_braket.types.program_set_validation_failure.ProgramSetValidationFailure"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProgramSetValidationFailuresList) -> list:
    import aws_sdk_braket.types.program_set_validation_failure

    out: list = []
    for item in value:
        out.append(
            aws_sdk_braket.types.program_set_validation_failure.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ProgramSetValidationFailuresList:
    import aws_sdk_braket.types.program_set_validation_failure

    out: ProgramSetValidationFailuresList = []
    for item in data:
        out.append(
            aws_sdk_braket.types.program_set_validation_failure.deserialize_json(item)
        )
    return out
