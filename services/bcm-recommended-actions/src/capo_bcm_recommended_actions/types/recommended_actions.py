"""Generated from Smithy shape ``com.amazonaws.bcmrecommendedactions#RecommendedActions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_recommended_actions.types.recommended_action

RecommendedActions: TypeAlias = list[
    "capo_bcm_recommended_actions.types.recommended_action.RecommendedAction"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RecommendedActions) -> list:
    import capo_bcm_recommended_actions.types.recommended_action

    out: list = []
    for item in value:
        out.append(
            capo_bcm_recommended_actions.types.recommended_action.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RecommendedActions:
    import capo_bcm_recommended_actions.types.recommended_action

    out: RecommendedActions = []
    for item in data:
        out.append(
            capo_bcm_recommended_actions.types.recommended_action.deserialize_aws_json_1_0(
                item
            )
        )
    return out
