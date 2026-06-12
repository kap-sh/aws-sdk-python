"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowAttributeOrConditionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_flow_attribute_and_condition

ContactFlowAttributeOrConditionList: TypeAlias = list[
    "aws_sdk_connect.types.contact_flow_attribute_and_condition.ContactFlowAttributeAndCondition"
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowAttributeOrConditionList) -> list:
    import aws_sdk_connect.types.contact_flow_attribute_and_condition

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.contact_flow_attribute_and_condition.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> ContactFlowAttributeOrConditionList:
    import aws_sdk_connect.types.contact_flow_attribute_and_condition

    out: ContactFlowAttributeOrConditionList = []
    for item in data:
        out.append(
            aws_sdk_connect.types.contact_flow_attribute_and_condition.deserialize_json(
                item
            )
        )
    return out
