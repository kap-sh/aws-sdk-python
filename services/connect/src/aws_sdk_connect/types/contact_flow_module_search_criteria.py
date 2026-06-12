"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowModuleSearchCriteria``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.contact_flow_module_search_condition_list
    import aws_sdk_connect.types.contact_flow_module_state
    import aws_sdk_connect.types.contact_flow_module_status
    import aws_sdk_connect.types.string_condition


class ContactFlowModuleSearchCriteria(TypedDict):
    or_conditions: NotRequired[
        "aws_sdk_connect.types.contact_flow_module_search_condition_list.ContactFlowModuleSearchConditionList"
    ]
    """<p>A list of conditions which would be applied together with an <code>OR</code> condition.</p>"""
    and_conditions: NotRequired[
        "aws_sdk_connect.types.contact_flow_module_search_condition_list.ContactFlowModuleSearchConditionList"
    ]
    """<p>A list of conditions which would be applied together with an <code>AND</code> condition.</p>"""
    string_condition: NotRequired[
        "aws_sdk_connect.types.string_condition.StringCondition"
    ]
    state_condition: NotRequired[
        "aws_sdk_connect.types.contact_flow_module_state.ContactFlowModuleState"
    ]
    """<p>The state of the flow.</p>"""
    status_condition: NotRequired[
        "aws_sdk_connect.types.contact_flow_module_status.ContactFlowModuleStatus"
    ]
    """<p>The status of the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowModuleSearchCriteria) -> dict:
    out: dict = {}
    if "or_conditions" in value:
        import aws_sdk_connect.types.contact_flow_module_search_condition_list

        out["OrConditions"] = (
            aws_sdk_connect.types.contact_flow_module_search_condition_list.serialize_json(
                value["or_conditions"]
            )
        )
    if "and_conditions" in value:
        import aws_sdk_connect.types.contact_flow_module_search_condition_list

        out["AndConditions"] = (
            aws_sdk_connect.types.contact_flow_module_search_condition_list.serialize_json(
                value["and_conditions"]
            )
        )
    if "string_condition" in value:
        import aws_sdk_connect.types.string_condition

        out["StringCondition"] = aws_sdk_connect.types.string_condition.serialize_json(
            value["string_condition"]
        )
    if "state_condition" in value:
        import aws_sdk_connect.types.contact_flow_module_state

        out["StateCondition"] = (
            aws_sdk_connect.types.contact_flow_module_state.serialize_json(
                value["state_condition"]
            )
        )
    if "status_condition" in value:
        import aws_sdk_connect.types.contact_flow_module_status

        out["StatusCondition"] = (
            aws_sdk_connect.types.contact_flow_module_status.serialize_json(
                value["status_condition"]
            )
        )
    return out


def deserialize_json(data: dict) -> ContactFlowModuleSearchCriteria:
    out: ContactFlowModuleSearchCriteria = {}  # type: ignore[typeddict-item]
    if "OrConditions" in data:
        import aws_sdk_connect.types.contact_flow_module_search_condition_list

        out["or_conditions"] = (
            aws_sdk_connect.types.contact_flow_module_search_condition_list.deserialize_json(
                data["OrConditions"]
            )
        )
    if "AndConditions" in data:
        import aws_sdk_connect.types.contact_flow_module_search_condition_list

        out["and_conditions"] = (
            aws_sdk_connect.types.contact_flow_module_search_condition_list.deserialize_json(
                data["AndConditions"]
            )
        )
    if "StringCondition" in data:
        import aws_sdk_connect.types.string_condition

        out["string_condition"] = (
            aws_sdk_connect.types.string_condition.deserialize_json(
                data["StringCondition"]
            )
        )
    if "StateCondition" in data:
        import aws_sdk_connect.types.contact_flow_module_state

        out["state_condition"] = (
            aws_sdk_connect.types.contact_flow_module_state.deserialize_json(
                data["StateCondition"]
            )
        )
    if "StatusCondition" in data:
        import aws_sdk_connect.types.contact_flow_module_status

        out["status_condition"] = (
            aws_sdk_connect.types.contact_flow_module_status.deserialize_json(
                data["StatusCondition"]
            )
        )
    return out
