"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowModuleSearchConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_flow_module_search_criteria

ContactFlowModuleSearchConditionList: TypeAlias = list[
    "aws_sdk_connect.types.contact_flow_module_search_criteria.ContactFlowModuleSearchCriteria"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowModuleSearchConditionList) -> list:
    import aws_sdk_connect.types.contact_flow_module_search_criteria

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.contact_flow_module_search_criteria.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ContactFlowModuleSearchConditionList:
    import aws_sdk_connect.types.contact_flow_module_search_criteria

    out: ContactFlowModuleSearchConditionList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.contact_flow_module_search_criteria.deserialize_json(
                item
            )
        )
    return out
