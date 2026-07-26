"""Generated from Smithy shape ``com.amazonaws.bcmrecommendedactions#ActionFilterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_recommended_actions.types.action_filter

ActionFilterList: TypeAlias = list[
    "capo_bcm_recommended_actions.types.action_filter.ActionFilter"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActionFilterList) -> list:
    import capo_bcm_recommended_actions.types.action_filter

    out: list = []
    for item in value:
        out.append(
            capo_bcm_recommended_actions.types.action_filter.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ActionFilterList:
    import capo_bcm_recommended_actions.types.action_filter

    out: ActionFilterList = []
    for item in data:
        out.append(
            capo_bcm_recommended_actions.types.action_filter.deserialize_aws_json_1_0(
                item
            )
        )
    return out
