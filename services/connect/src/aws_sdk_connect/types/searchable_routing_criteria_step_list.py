"""Generated from Smithy shape ``com.amazonaws.connect#SearchableRoutingCriteriaStepList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.searchable_routing_criteria_step

SearchableRoutingCriteriaStepList: TypeAlias = list[
    "aws_sdk_connect.types.searchable_routing_criteria_step.SearchableRoutingCriteriaStep"
]


# --- restJson1 ser/de ---
def serialize_json(value: SearchableRoutingCriteriaStepList) -> list:
    import aws_sdk_connect.types.searchable_routing_criteria_step

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.searchable_routing_criteria_step.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SearchableRoutingCriteriaStepList:
    import aws_sdk_connect.types.searchable_routing_criteria_step

    out: SearchableRoutingCriteriaStepList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.searchable_routing_criteria_step.deserialize_json(
                item
            )
        )
    return out
