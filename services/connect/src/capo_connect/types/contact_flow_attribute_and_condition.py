"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowAttributeAndCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_flow_type_condition
    import capo_connect.types.tag_and_condition_list


class ContactFlowAttributeAndCondition(TypedDict, closed=True):
    tag_conditions: NotRequired[
        "capo_connect.types.tag_and_condition_list.TagAndConditionList"
    ]
    """<p> Tag-based conditions for contact flow filtering.</p>"""
    contact_flow_type_condition: NotRequired[
        "capo_connect.types.contact_flow_type_condition.ContactFlowTypeCondition"
    ]
    """<p> Contact flow type condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowAttributeAndCondition) -> dict:
    out: dict = {}
    if "tag_conditions" in value:
        import capo_connect.types.tag_and_condition_list

        out["TagConditions"] = capo_connect.types.tag_and_condition_list.serialize_json(
            value["tag_conditions"]
        )
    if "contact_flow_type_condition" in value:
        import capo_connect.types.contact_flow_type_condition

        out["ContactFlowTypeCondition"] = (
            capo_connect.types.contact_flow_type_condition.serialize_json(
                value["contact_flow_type_condition"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContactFlowAttributeAndCondition:
    out: ContactFlowAttributeAndCondition = {}  # type: ignore[typeddict-item]
    if "TagConditions" in data:
        import capo_connect.types.tag_and_condition_list

        out["tag_conditions"] = (
            capo_connect.types.tag_and_condition_list.deserialize_json(
                data["TagConditions"]
            )
        )
    if "ContactFlowTypeCondition" in data:
        import capo_connect.types.contact_flow_type_condition

        out["contact_flow_type_condition"] = (
            capo_connect.types.contact_flow_type_condition.deserialize_json(
                data["ContactFlowTypeCondition"]
            )
        )
    return out
