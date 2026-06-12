"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#InferenceSchedulerSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.inference_scheduler_summary

InferenceSchedulerSummaries: TypeAlias = list[
    "aws_sdk_lookoutequipment.types.inference_scheduler_summary.InferenceSchedulerSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InferenceSchedulerSummaries) -> list:
    import aws_sdk_lookoutequipment.types.inference_scheduler_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lookoutequipment.types.inference_scheduler_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> InferenceSchedulerSummaries:
    import aws_sdk_lookoutequipment.types.inference_scheduler_summary

    out: InferenceSchedulerSummaries = []
    for item in data:
        out.append(
            aws_sdk_lookoutequipment.types.inference_scheduler_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
