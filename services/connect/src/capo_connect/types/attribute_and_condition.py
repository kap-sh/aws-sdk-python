"""Generated from Smithy shape ``com.amazonaws.connect#AttributeAndCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.hierarchy_group_condition
    import capo_connect.types.tag_and_condition_list


class AttributeAndCondition(TypedDict, closed=True):
    tag_conditions: NotRequired[
        "capo_connect.types.tag_and_condition_list.TagAndConditionList"
    ]
    """<p>A leaf node condition which can be used to specify a tag condition.</p>"""
    hierarchy_group_condition: NotRequired[
        "capo_connect.types.hierarchy_group_condition.HierarchyGroupCondition"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: AttributeAndCondition) -> dict:
    out: dict = {}
    if "tag_conditions" in value:
        import capo_connect.types.tag_and_condition_list

        out["TagConditions"] = capo_connect.types.tag_and_condition_list.serialize_json(
            value["tag_conditions"]
        )
    if "hierarchy_group_condition" in value:
        import capo_connect.types.hierarchy_group_condition

        out["HierarchyGroupCondition"] = (
            capo_connect.types.hierarchy_group_condition.serialize_json(
                value["hierarchy_group_condition"]
            )
        )
    return out


def deserialize_json(data: dict) -> AttributeAndCondition:
    out: AttributeAndCondition = {}  # type: ignore[typeddict-item]
    if "TagConditions" in data:
        import capo_connect.types.tag_and_condition_list

        out["tag_conditions"] = (
            capo_connect.types.tag_and_condition_list.deserialize_json(
                data["TagConditions"]
            )
        )
    if "HierarchyGroupCondition" in data:
        import capo_connect.types.hierarchy_group_condition

        out["hierarchy_group_condition"] = (
            capo_connect.types.hierarchy_group_condition.deserialize_json(
                data["HierarchyGroupCondition"]
            )
        )
    return out
