"""Generated from Smithy shape ``com.amazonaws.connect#UserSearchCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.hierarchy_group_condition
    import capo_connect.types.list_condition
    import capo_connect.types.string_condition
    import capo_connect.types.user_search_condition_list


class UserSearchCriteria(TypedDict, closed=True):
    or_conditions: NotRequired[
        "capo_connect.types.user_search_condition_list.UserSearchConditionList"
    ]
    """<p>A list of conditions which would be applied together with an <code>OR</code> condition.</p>"""
    and_conditions: NotRequired[
        "capo_connect.types.user_search_condition_list.UserSearchConditionList"
    ]
    """<p>A list of conditions which would be applied together with an <code>AND</code> condition.</p>"""
    string_condition: NotRequired["capo_connect.types.string_condition.StringCondition"]
    """<p>A leaf node condition which can be used to specify a string condition.</p> <p>The currently supported values for <code>FieldName</code> are <code>Username</code>, <code>FirstName</code>, <code>LastName</code>, <code>RoutingProfileId</code>, <code>SecurityProfileId</code>, <code>resourceId</code>.</p>"""
    list_condition: NotRequired["capo_connect.types.list_condition.ListCondition"]
    """<p>A leaf node condition which can be used to specify a List condition to search users with attributes included in Lists like Proficiencies.</p>"""
    hierarchy_group_condition: NotRequired[
        "capo_connect.types.hierarchy_group_condition.HierarchyGroupCondition"
    ]
    """<p>A leaf node condition which can be used to specify a hierarchy group condition.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserSearchCriteria) -> dict:
    out: dict = {}
    if "or_conditions" in value:
        import capo_connect.types.user_search_condition_list

        out["OrConditions"] = (
            capo_connect.types.user_search_condition_list.serialize_json(
                value["or_conditions"]
            )
        )
    if "and_conditions" in value:
        import capo_connect.types.user_search_condition_list

        out["AndConditions"] = (
            capo_connect.types.user_search_condition_list.serialize_json(
                value["and_conditions"]
            )
        )
    if "string_condition" in value:
        import capo_connect.types.string_condition

        out["StringCondition"] = capo_connect.types.string_condition.serialize_json(
            value["string_condition"]
        )
    if "list_condition" in value:
        import capo_connect.types.list_condition

        out["ListCondition"] = capo_connect.types.list_condition.serialize_json(
            value["list_condition"]
        )
    if "hierarchy_group_condition" in value:
        import capo_connect.types.hierarchy_group_condition

        out["HierarchyGroupCondition"] = (
            capo_connect.types.hierarchy_group_condition.serialize_json(
                value["hierarchy_group_condition"]
            )
        )
    return out


def deserialize_json(data: dict) -> UserSearchCriteria:
    out: UserSearchCriteria = {}  # type: ignore[typeddict-item]
    if "OrConditions" in data:
        import capo_connect.types.user_search_condition_list

        out["or_conditions"] = (
            capo_connect.types.user_search_condition_list.deserialize_json(
                data["OrConditions"]
            )
        )
    if "AndConditions" in data:
        import capo_connect.types.user_search_condition_list

        out["and_conditions"] = (
            capo_connect.types.user_search_condition_list.deserialize_json(
                data["AndConditions"]
            )
        )
    if "StringCondition" in data:
        import capo_connect.types.string_condition

        out["string_condition"] = capo_connect.types.string_condition.deserialize_json(
            data["StringCondition"]
        )
    if "ListCondition" in data:
        import capo_connect.types.list_condition

        out["list_condition"] = capo_connect.types.list_condition.deserialize_json(
            data["ListCondition"]
        )
    if "HierarchyGroupCondition" in data:
        import capo_connect.types.hierarchy_group_condition

        out["hierarchy_group_condition"] = (
            capo_connect.types.hierarchy_group_condition.deserialize_json(
                data["HierarchyGroupCondition"]
            )
        )
    return out
