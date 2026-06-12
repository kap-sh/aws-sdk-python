"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ComputationModelExecutionSummary``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.computation_model_execution_summary_key
    import aws_sdk_iotsitewise.types.computation_model_execution_summary_value

ComputationModelExecutionSummary: TypeAlias = dict[
    "aws_sdk_iotsitewise.types.computation_model_execution_summary_key.ComputationModelExecutionSummaryKey",
    "aws_sdk_iotsitewise.types.computation_model_execution_summary_value.ComputationModelExecutionSummaryValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ComputationModelExecutionSummary) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ComputationModelExecutionSummary:
    out: ComputationModelExecutionSummary = {}
    for key, value in data.items():
        out[key] = value
    return out
