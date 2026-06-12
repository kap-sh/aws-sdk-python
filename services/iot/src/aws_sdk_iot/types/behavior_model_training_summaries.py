"""Generated from Smithy shape ``com.amazonaws.iot#BehaviorModelTrainingSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.behavior_model_training_summary

BehaviorModelTrainingSummaries: TypeAlias = list[
    "aws_sdk_iot.types.behavior_model_training_summary.BehaviorModelTrainingSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: BehaviorModelTrainingSummaries) -> list:
    import aws_sdk_iot.types.behavior_model_training_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot.types.behavior_model_training_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> BehaviorModelTrainingSummaries:
    import aws_sdk_iot.types.behavior_model_training_summary

    out: BehaviorModelTrainingSummaries = []
    for item in data:
        out.append(
            aws_sdk_iot.types.behavior_model_training_summary.deserialize_json(item)
        )
    return out
