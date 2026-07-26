"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#RecommendedActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_compute_optimizer_automation.types.recommended_action

RecommendedActions: TypeAlias = list[
    "capo_compute_optimizer_automation.types.recommended_action.RecommendedAction"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendedActions) -> list:
    import capo_compute_optimizer_automation.types.recommended_action

    out: list = []
    for item in value:
        out.append(
            capo_compute_optimizer_automation.types.recommended_action.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RecommendedActions:
    import capo_compute_optimizer_automation.types.recommended_action

    out: RecommendedActions = []
    for item in data:
        out.append(
            capo_compute_optimizer_automation.types.recommended_action.deserialize_aws_json_1_0(
                item
            )
        )
    return out
