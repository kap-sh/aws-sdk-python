"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#InferenceExecutionSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.inference_execution_summary

InferenceExecutionSummaries: TypeAlias = list[
    "aws_sdk_lookoutequipment.types.inference_execution_summary.InferenceExecutionSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InferenceExecutionSummaries) -> list:
    import aws_sdk_lookoutequipment.types.inference_execution_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lookoutequipment.types.inference_execution_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> InferenceExecutionSummaries:
    import aws_sdk_lookoutequipment.types.inference_execution_summary

    out: InferenceExecutionSummaries = []
    for item in data:
        out.append(
            aws_sdk_lookoutequipment.types.inference_execution_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
