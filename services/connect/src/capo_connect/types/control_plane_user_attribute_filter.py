"""Generated from Smithy shape ``com.amazonaws.connect#ControlPlaneUserAttributeFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.attribute_and_condition
    import capo_connect.types.attribute_or_condition_list
    import capo_connect.types.hierarchy_group_condition
    import capo_connect.types.tag_condition


class ControlPlaneUserAttributeFilter(TypedDict, closed=True):
    or_conditions: NotRequired[
        "capo_connect.types.attribute_or_condition_list.AttributeOrConditionList"
    ]
    """<p>A list of conditions which would be applied together with an <code>OR</code> condition.</p>"""
    and_condition: NotRequired[
        "capo_connect.types.attribute_and_condition.AttributeAndCondition"
    ]
    """<p>A list of conditions which would be applied together with an <code>AND</code> condition.</p>"""
    tag_condition: NotRequired["capo_connect.types.tag_condition.TagCondition"]
    hierarchy_group_condition: NotRequired[
        "capo_connect.types.hierarchy_group_condition.HierarchyGroupCondition"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ControlPlaneUserAttributeFilter) -> dict:
    out: dict = {}
    if "or_conditions" in value:
        import capo_connect.types.attribute_or_condition_list

        out["OrConditions"] = (
            capo_connect.types.attribute_or_condition_list.serialize_json(
                value["or_conditions"]
            )
        )
    if "and_condition" in value:
        import capo_connect.types.attribute_and_condition

        out["AndCondition"] = capo_connect.types.attribute_and_condition.serialize_json(
            value["and_condition"]
        )
    if "tag_condition" in value:
        import capo_connect.types.tag_condition

        out["TagCondition"] = capo_connect.types.tag_condition.serialize_json(
            value["tag_condition"]
        )
    if "hierarchy_group_condition" in value:
        import capo_connect.types.hierarchy_group_condition

        out["HierarchyGroupCondition"] = (
            capo_connect.types.hierarchy_group_condition.serialize_json(
                value["hierarchy_group_condition"]
            )
        )
    return out


def deserialize_json(data: dict) -> ControlPlaneUserAttributeFilter:
    out: ControlPlaneUserAttributeFilter = {}  # type: ignore[typeddict-item]
    if "OrConditions" in data:
        import capo_connect.types.attribute_or_condition_list

        out["or_conditions"] = (
            capo_connect.types.attribute_or_condition_list.deserialize_json(
                data["OrConditions"]
            )
        )
    if "AndCondition" in data:
        import capo_connect.types.attribute_and_condition

        out["and_condition"] = (
            capo_connect.types.attribute_and_condition.deserialize_json(
                data["AndCondition"]
            )
        )
    if "TagCondition" in data:
        import capo_connect.types.tag_condition

        out["tag_condition"] = capo_connect.types.tag_condition.deserialize_json(
            data["TagCondition"]
        )
    if "HierarchyGroupCondition" in data:
        import capo_connect.types.hierarchy_group_condition

        out["hierarchy_group_condition"] = (
            capo_connect.types.hierarchy_group_condition.deserialize_json(
                data["HierarchyGroupCondition"]
            )
        )
    return out
