"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowAttributeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_flow_attribute_and_condition
    import capo_connect.types.contact_flow_attribute_or_condition_list
    import capo_connect.types.contact_flow_type_condition
    import capo_connect.types.tag_condition


class ContactFlowAttributeFilter(TypedDict, closed=True):
    or_conditions: NotRequired[
        "capo_connect.types.contact_flow_attribute_or_condition_list.ContactFlowAttributeOrConditionList"
    ]
    """<p> A list of conditions which would be applied together with an OR condition.</p>"""
    and_condition: NotRequired[
        "capo_connect.types.contact_flow_attribute_and_condition.ContactFlowAttributeAndCondition"
    ]
    """<p> A list of conditions which would be applied together with a AND condition.</p>"""
    tag_condition: NotRequired["capo_connect.types.tag_condition.TagCondition"]
    contact_flow_type_condition: NotRequired[
        "capo_connect.types.contact_flow_type_condition.ContactFlowTypeCondition"
    ]
    """<p> Contact flow type condition within attribute filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowAttributeFilter) -> dict:
    out: dict = {}
    if "or_conditions" in value:
        import capo_connect.types.contact_flow_attribute_or_condition_list

        out["OrConditions"] = (
            capo_connect.types.contact_flow_attribute_or_condition_list.serialize_json(
                value["or_conditions"]
            )
        )
    if "and_condition" in value:
        import capo_connect.types.contact_flow_attribute_and_condition

        out["AndCondition"] = (
            capo_connect.types.contact_flow_attribute_and_condition.serialize_json(
                value["and_condition"]
            )
        )
    if "tag_condition" in value:
        import capo_connect.types.tag_condition

        out["TagCondition"] = capo_connect.types.tag_condition.serialize_json(
            value["tag_condition"]
        )
    if "contact_flow_type_condition" in value:
        import capo_connect.types.contact_flow_type_condition

        out["ContactFlowTypeCondition"] = (
            capo_connect.types.contact_flow_type_condition.serialize_json(
                value["contact_flow_type_condition"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContactFlowAttributeFilter:
    out: ContactFlowAttributeFilter = {}  # type: ignore[typeddict-item]
    if "OrConditions" in data:
        import capo_connect.types.contact_flow_attribute_or_condition_list

        out["or_conditions"] = (
            capo_connect.types.contact_flow_attribute_or_condition_list.deserialize_json(
                data["OrConditions"]
            )
        )
    if "AndCondition" in data:
        import capo_connect.types.contact_flow_attribute_and_condition

        out["and_condition"] = (
            capo_connect.types.contact_flow_attribute_and_condition.deserialize_json(
                data["AndCondition"]
            )
        )
    if "TagCondition" in data:
        import capo_connect.types.tag_condition

        out["tag_condition"] = capo_connect.types.tag_condition.deserialize_json(
            data["TagCondition"]
        )
    if "ContactFlowTypeCondition" in data:
        import capo_connect.types.contact_flow_type_condition

        out["contact_flow_type_condition"] = (
            capo_connect.types.contact_flow_type_condition.deserialize_json(
                data["ContactFlowTypeCondition"]
            )
        )
    return out
