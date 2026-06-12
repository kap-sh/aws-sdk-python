"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ComputationModelSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.computation_model_summary

ComputationModelSummaries: TypeAlias = list[
    "aws_sdk_iotsitewise.types.computation_model_summary.ComputationModelSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: ComputationModelSummaries) -> list:
    import aws_sdk_iotsitewise.types.computation_model_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iotsitewise.types.computation_model_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ComputationModelSummaries:
    import aws_sdk_iotsitewise.types.computation_model_summary

    out: ComputationModelSummaries = []
    for item in data:
        out.append(
            aws_sdk_iotsitewise.types.computation_model_summary.deserialize_json(item)
        )
    return out
