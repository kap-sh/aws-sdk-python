"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#RecommendedActionFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer_automation.types.recommended_action_filter

RecommendedActionFilterList: TypeAlias = list[
    "aws_sdk_compute_optimizer_automation.types.recommended_action_filter.RecommendedActionFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendedActionFilterList) -> list:
    import aws_sdk_compute_optimizer_automation.types.recommended_action_filter

    out: list = []
    for item in value:
        out.append(
            aws_sdk_compute_optimizer_automation.types.recommended_action_filter.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RecommendedActionFilterList:
    import aws_sdk_compute_optimizer_automation.types.recommended_action_filter

    out: RecommendedActionFilterList = []
    for item in data:
        out.append(
            aws_sdk_compute_optimizer_automation.types.recommended_action_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out
