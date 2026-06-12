"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#RetrainingSchedulerSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_lookoutequipment.types.retraining_scheduler_summary

RetrainingSchedulerSummaries: TypeAlias = list[
    "aws_sdk_lookoutequipment.types.retraining_scheduler_summary.RetrainingSchedulerSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RetrainingSchedulerSummaries) -> list:
    import aws_sdk_lookoutequipment.types.retraining_scheduler_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_lookoutequipment.types.retraining_scheduler_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RetrainingSchedulerSummaries:
    import aws_sdk_lookoutequipment.types.retraining_scheduler_summary

    out: RetrainingSchedulerSummaries = []
    for item in data:
        out.append(
            aws_sdk_lookoutequipment.types.retraining_scheduler_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
