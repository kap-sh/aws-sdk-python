"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowAttributeOrConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.contact_flow_attribute_and_condition

ContactFlowAttributeOrConditionList: TypeAlias = list[
    "capo_connect.types.contact_flow_attribute_and_condition.ContactFlowAttributeAndCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowAttributeOrConditionList) -> list:
    import capo_connect.types.contact_flow_attribute_and_condition

    out: list = []
    for item in value:
        out.append(
            capo_connect.types.contact_flow_attribute_and_condition.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ContactFlowAttributeOrConditionList:
    import capo_connect.types.contact_flow_attribute_and_condition

    out: ContactFlowAttributeOrConditionList = []
    for item in data:
        out.append(
            capo_connect.types.contact_flow_attribute_and_condition.deserialize_json(
                item
            )
        )
    return out
