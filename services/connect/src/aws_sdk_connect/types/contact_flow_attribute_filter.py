"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowAttributeFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_flow_attribute_and_condition
    import aws_sdk_connect.types.contact_flow_attribute_or_condition_list
    import aws_sdk_connect.types.contact_flow_type_condition
    import aws_sdk_connect.types.tag_condition


class ContactFlowAttributeFilter(TypedDict):
    or_conditions: NotRequired[
        "aws_sdk_connect.types.contact_flow_attribute_or_condition_list.ContactFlowAttributeOrConditionList"
    ]
    """<p> A list of conditions which would be applied together with an OR condition.</p>"""
    and_condition: NotRequired[
        "aws_sdk_connect.types.contact_flow_attribute_and_condition.ContactFlowAttributeAndCondition"
    ]
    """<p> A list of conditions which would be applied together with a AND condition.</p>"""
    tag_condition: NotRequired["aws_sdk_connect.types.tag_condition.TagCondition"]
    contact_flow_type_condition: NotRequired[
        "aws_sdk_connect.types.contact_flow_type_condition.ContactFlowTypeCondition"
    ]
    """<p> Contact flow type condition within attribute filter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowAttributeFilter) -> dict:
    out: dict = {}
    if "or_conditions" in value:
        import aws_sdk_connect.types.contact_flow_attribute_or_condition_list

        out["OrConditions"] = (
            aws_sdk_connect.types.contact_flow_attribute_or_condition_list.serialize_json(
                value["or_conditions"]
            )
        )
    if "and_condition" in value:
        import aws_sdk_connect.types.contact_flow_attribute_and_condition

        out["AndCondition"] = (
            aws_sdk_connect.types.contact_flow_attribute_and_condition.serialize_json(
                value["and_condition"]
            )
        )
    if "tag_condition" in value:
        import aws_sdk_connect.types.tag_condition

        out["TagCondition"] = aws_sdk_connect.types.tag_condition.serialize_json(
            value["tag_condition"]
        )
    if "contact_flow_type_condition" in value:
        import aws_sdk_connect.types.contact_flow_type_condition

        out["ContactFlowTypeCondition"] = (
            aws_sdk_connect.types.contact_flow_type_condition.serialize_json(
                value["contact_flow_type_condition"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContactFlowAttributeFilter:
    out: ContactFlowAttributeFilter = {}  # type: ignore[typeddict-item]
    if "OrConditions" in data:
        import aws_sdk_connect.types.contact_flow_attribute_or_condition_list

        out["or_conditions"] = (
            aws_sdk_connect.types.contact_flow_attribute_or_condition_list.deserialize_json(
                data["OrConditions"]
            )
        )
    if "AndCondition" in data:
        import aws_sdk_connect.types.contact_flow_attribute_and_condition

        out["and_condition"] = (
            aws_sdk_connect.types.contact_flow_attribute_and_condition.deserialize_json(
                data["AndCondition"]
            )
        )
    if "TagCondition" in data:
        import aws_sdk_connect.types.tag_condition

        out["tag_condition"] = aws_sdk_connect.types.tag_condition.deserialize_json(
            data["TagCondition"]
        )
    if "ContactFlowTypeCondition" in data:
        import aws_sdk_connect.types.contact_flow_type_condition

        out["contact_flow_type_condition"] = (
            aws_sdk_connect.types.contact_flow_type_condition.deserialize_json(
                data["ContactFlowTypeCondition"]
            )
        )
    return out
