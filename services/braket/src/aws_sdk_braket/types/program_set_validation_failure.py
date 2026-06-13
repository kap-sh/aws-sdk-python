"""Generated from Smithy shape ``com.amazonaws.braket#ProgramSetValidationFailure``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_braket.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_braket.types.program_validation_failures_list


class ProgramSetValidationFailure(TypedDict):
    program_index: "int"
    """<p>The index of the program within the program set that failed validation.</p>"""
    inputs_index: NotRequired["int"]
    """<p>The index of the input within the program set that failed validation.</p>"""
    errors: NotRequired[
        "aws_sdk_braket.types.program_validation_failures_list.ProgramValidationFailuresList"
    ]
    """<p>A list of error messages describing the validation failures that occurred.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProgramSetValidationFailure) -> dict:
    out: dict = {}
    out["programIndex"] = value["program_index"]
    if "inputs_index" in value:
        out["inputsIndex"] = value["inputs_index"]
    if "errors" in value:
        import aws_sdk_braket.types.program_validation_failures_list

        out["errors"] = (
            aws_sdk_braket.types.program_validation_failures_list.serialize_json(
                value["errors"]
            )
        )
    return out


def deserialize_json(data: dict) -> ProgramSetValidationFailure:
    out: ProgramSetValidationFailure = {}  # type: ignore[typeddict-item]
    if "programIndex" in data:
        out["program_index"] = data["programIndex"]
    else:
        raise DeserializationError("ProgramSetValidationFailure.program_index required")
    if "inputsIndex" in data:
        out["inputs_index"] = data["inputsIndex"]
    if "errors" in data:
        import aws_sdk_braket.types.program_validation_failures_list

        out["errors"] = (
            aws_sdk_braket.types.program_validation_failures_list.deserialize_json(
                data["errors"]
            )
        )
    return out
