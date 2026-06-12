"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowAttributeAndCondition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_flow_type_condition
    import aws_sdk_connect.types.tag_and_condition_list


class ContactFlowAttributeAndCondition(TypedDict):
    tag_conditions: NotRequired[
        "aws_sdk_connect.types.tag_and_condition_list.TagAndConditionList"
    ]
    """<p> Tag-based conditions for contact flow filtering.</p>"""
    contact_flow_type_condition: NotRequired[
        "aws_sdk_connect.types.contact_flow_type_condition.ContactFlowTypeCondition"
    ]
    """<p> Contact flow type condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowAttributeAndCondition) -> dict:
    out: dict = {}
    if "tag_conditions" in value:
        import aws_sdk_connect.types.tag_and_condition_list

        out["TagConditions"] = (
            aws_sdk_connect.types.tag_and_condition_list.serialize_json(
                value["tag_conditions"]
            )
        )
    if "contact_flow_type_condition" in value:
        import aws_sdk_connect.types.contact_flow_type_condition

        out["ContactFlowTypeCondition"] = (
            aws_sdk_connect.types.contact_flow_type_condition.serialize_json(
                value["contact_flow_type_condition"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContactFlowAttributeAndCondition:
    out: ContactFlowAttributeAndCondition = {}  # type: ignore[typeddict-item]
    if "TagConditions" in data:
        import aws_sdk_connect.types.tag_and_condition_list

        out["tag_conditions"] = (
            aws_sdk_connect.types.tag_and_condition_list.deserialize_json(
                data["TagConditions"]
            )
        )
    if "ContactFlowTypeCondition" in data:
        import aws_sdk_connect.types.contact_flow_type_condition

        out["contact_flow_type_condition"] = (
            aws_sdk_connect.types.contact_flow_type_condition.deserialize_json(
                data["ContactFlowTypeCondition"]
            )
        )
    return out
