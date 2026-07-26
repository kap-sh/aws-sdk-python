"""Generated from Smithy shape ``com.amazonaws.connect#ContactFlowSearchCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_flow_search_condition_list
    import capo_connect.types.contact_flow_state
    import capo_connect.types.contact_flow_status
    import capo_connect.types.contact_flow_type
    import capo_connect.types.string_condition


class ContactFlowSearchCriteria(TypedDict, closed=True):
    or_conditions: NotRequired[
        "capo_connect.types.contact_flow_search_condition_list.ContactFlowSearchConditionList"
    ]
    """<p>A list of conditions which would be applied together with an <code>OR</code> condition.</p>"""
    and_conditions: NotRequired[
        "capo_connect.types.contact_flow_search_condition_list.ContactFlowSearchConditionList"
    ]
    """<p>A list of conditions which would be applied together with an <code>AND</code> condition.</p>"""
    string_condition: NotRequired["capo_connect.types.string_condition.StringCondition"]
    type_condition: NotRequired["capo_connect.types.contact_flow_type.ContactFlowType"]
    """<p>The type of flow.</p>"""
    state_condition: NotRequired[
        "capo_connect.types.contact_flow_state.ContactFlowState"
    ]
    """<p>The state of the flow.</p>"""
    status_condition: NotRequired[
        "capo_connect.types.contact_flow_status.ContactFlowStatus"
    ]
    """<p>The status of the flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactFlowSearchCriteria) -> dict:
    out: dict = {}
    if "or_conditions" in value:
        import capo_connect.types.contact_flow_search_condition_list

        out["OrConditions"] = (
            capo_connect.types.contact_flow_search_condition_list.serialize_json(
                value["or_conditions"]
            )
        )
    if "and_conditions" in value:
        import capo_connect.types.contact_flow_search_condition_list

        out["AndConditions"] = (
            capo_connect.types.contact_flow_search_condition_list.serialize_json(
                value["and_conditions"]
            )
        )
    if "string_condition" in value:
        import capo_connect.types.string_condition

        out["StringCondition"] = capo_connect.types.string_condition.serialize_json(
            value["string_condition"]
        )
    if "type_condition" in value:
        import capo_connect.types.contact_flow_type

        out["TypeCondition"] = capo_connect.types.contact_flow_type.serialize_json(
            value["type_condition"]
        )
    if "state_condition" in value:
        import capo_connect.types.contact_flow_state

        out["StateCondition"] = capo_connect.types.contact_flow_state.serialize_json(
            value["state_condition"]
        )
    if "status_condition" in value:
        import capo_connect.types.contact_flow_status

        out["StatusCondition"] = capo_connect.types.contact_flow_status.serialize_json(
            value["status_condition"]
        )
    return out


def deserialize_json(data: dict) -> ContactFlowSearchCriteria:
    out: ContactFlowSearchCriteria = {}  # type: ignore[typeddict-item]
    if "OrConditions" in data:
        import capo_connect.types.contact_flow_search_condition_list

        out["or_conditions"] = (
            capo_connect.types.contact_flow_search_condition_list.deserialize_json(
                data["OrConditions"]
            )
        )
    if "AndConditions" in data:
        import capo_connect.types.contact_flow_search_condition_list

        out["and_conditions"] = (
            capo_connect.types.contact_flow_search_condition_list.deserialize_json(
                data["AndConditions"]
            )
        )
    if "StringCondition" in data:
        import capo_connect.types.string_condition

        out["string_condition"] = capo_connect.types.string_condition.deserialize_json(
            data["StringCondition"]
        )
    if "TypeCondition" in data:
        import capo_connect.types.contact_flow_type

        out["type_condition"] = capo_connect.types.contact_flow_type.deserialize_json(
            data["TypeCondition"]
        )
    if "StateCondition" in data:
        import capo_connect.types.contact_flow_state

        out["state_condition"] = capo_connect.types.contact_flow_state.deserialize_json(
            data["StateCondition"]
        )
    if "StatusCondition" in data:
        import capo_connect.types.contact_flow_status

        out["status_condition"] = (
            capo_connect.types.contact_flow_status.deserialize_json(
                data["StatusCondition"]
            )
        )
    return out
