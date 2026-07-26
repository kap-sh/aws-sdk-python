"""Generated from Smithy shape ``com.amazonaws.connect#WorkspaceAssociationSearchCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.string_condition
    import capo_connect.types.workspace_association_search_condition_list


class WorkspaceAssociationSearchCriteria(TypedDict, closed=True):
    or_conditions: NotRequired[
        "capo_connect.types.workspace_association_search_condition_list.WorkspaceAssociationSearchConditionList"
    ]
    """<p>A list of conditions to be met, where at least one condition must be satisfied.</p>"""
    and_conditions: NotRequired[
        "capo_connect.types.workspace_association_search_condition_list.WorkspaceAssociationSearchConditionList"
    ]
    """<p>A list of conditions that must all be satisfied.</p>"""
    string_condition: NotRequired["capo_connect.types.string_condition.StringCondition"]


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceAssociationSearchCriteria) -> dict:
    out: dict = {}
    if "or_conditions" in value:
        import capo_connect.types.workspace_association_search_condition_list

        out["OrConditions"] = (
            capo_connect.types.workspace_association_search_condition_list.serialize_json(
                value["or_conditions"]
            )
        )
    if "and_conditions" in value:
        import capo_connect.types.workspace_association_search_condition_list

        out["AndConditions"] = (
            capo_connect.types.workspace_association_search_condition_list.serialize_json(
                value["and_conditions"]
            )
        )
    if "string_condition" in value:
        import capo_connect.types.string_condition

        out["StringCondition"] = capo_connect.types.string_condition.serialize_json(
            value["string_condition"]
        )
    return out


def deserialize_json(data: dict) -> WorkspaceAssociationSearchCriteria:
    out: WorkspaceAssociationSearchCriteria = {}  # type: ignore[typeddict-item]
    if "OrConditions" in data:
        import capo_connect.types.workspace_association_search_condition_list

        out["or_conditions"] = (
            capo_connect.types.workspace_association_search_condition_list.deserialize_json(
                data["OrConditions"]
            )
        )
    if "AndConditions" in data:
        import capo_connect.types.workspace_association_search_condition_list

        out["and_conditions"] = (
            capo_connect.types.workspace_association_search_condition_list.deserialize_json(
                data["AndConditions"]
            )
        )
    if "StringCondition" in data:
        import capo_connect.types.string_condition

        out["string_condition"] = capo_connect.types.string_condition.deserialize_json(
            data["StringCondition"]
        )
    return out
