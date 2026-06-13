"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#StepInputParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_migrationhuborchestrator.types.step_input
    import aws_sdk_migrationhuborchestrator.types.step_input_parameters_key

StepInputParameters: TypeAlias = dict[
    "aws_sdk_migrationhuborchestrator.types.step_input_parameters_key.StepInputParametersKey",
    "aws_sdk_migrationhuborchestrator.types.step_input.StepInput",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: StepInputParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_migrationhuborchestrator.types.step_input

        out[key] = aws_sdk_migrationhuborchestrator.types.step_input.serialize_json(
            value
        )
    return out


def deserialize_json(data: dict) -> StepInputParameters:
    out: StepInputParameters = {}
    for key, value in data.items():
        import aws_sdk_migrationhuborchestrator.types.step_input

        out[key] = aws_sdk_migrationhuborchestrator.types.step_input.deserialize_json(
            value
        )
    return out
