"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowSearchConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_flow_search_criteria

ContactFlowSearchConditionList: TypeAlias = list[
    "aws_sdk_connect.types.contact_flow_search_criteria.ContactFlowSearchCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowSearchConditionList) -> list:
    import aws_sdk_connect.types.contact_flow_search_criteria

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.contact_flow_search_criteria.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ContactFlowSearchConditionList:
    import aws_sdk_connect.types.contact_flow_search_criteria

    out: ContactFlowSearchConditionList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.contact_flow_search_criteria.deserialize_json(item)
        )
    return out
