"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowSearchConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.contact_flow_search_criteria

ContactFlowSearchConditionList: TypeAlias = list[
    "capo_connect.types.contact_flow_search_criteria.ContactFlowSearchCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowSearchConditionList) -> list:
    import capo_connect.types.contact_flow_search_criteria

    out: list = []
    for item in value:
        out.append(capo_connect.types.contact_flow_search_criteria.serialize_json(item))
    return out


def deserialize_json(data: list) -> ContactFlowSearchConditionList:
    import capo_connect.types.contact_flow_search_criteria

    out: ContactFlowSearchConditionList = []
    for item in data:
        out.append(
            capo_connect.types.contact_flow_search_criteria.deserialize_json(item)
        )
    return out
