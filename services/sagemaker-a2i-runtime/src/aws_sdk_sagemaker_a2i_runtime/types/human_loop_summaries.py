"""Generated from Smithy shape ``com.amazonaws.sagemakera2iruntime#HumanLoopSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker_a2i_runtime.types.human_loop_summary

HumanLoopSummaries: TypeAlias = list[
    "aws_sdk_sagemaker_a2i_runtime.types.human_loop_summary.HumanLoopSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: HumanLoopSummaries) -> list:
    import aws_sdk_sagemaker_a2i_runtime.types.human_loop_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_sagemaker_a2i_runtime.types.human_loop_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> HumanLoopSummaries:
    import aws_sdk_sagemaker_a2i_runtime.types.human_loop_summary

    out: HumanLoopSummaries = []
    for item in data:
        out.append(
            aws_sdk_sagemaker_a2i_runtime.types.human_loop_summary.deserialize_json(
                item
            )
        )
    return out
