"""Generated from Smithy shape ``com.amazonaws.connect#ControlPlaneUserAttributeFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.attribute_and_condition
    import aws_sdk_connect.types.attribute_or_condition_list
    import aws_sdk_connect.types.hierarchy_group_condition
    import aws_sdk_connect.types.tag_condition


class ControlPlaneUserAttributeFilter(TypedDict):
    or_conditions: NotRequired[
        "aws_sdk_connect.types.attribute_or_condition_list.AttributeOrConditionList"
    ]
    """<p>A list of conditions which would be applied together with an <code>OR</code> condition.</p>"""
    and_condition: NotRequired[
        "aws_sdk_connect.types.attribute_and_condition.AttributeAndCondition"
    ]
    """<p>A list of conditions which would be applied together with an <code>AND</code> condition.</p>"""
    tag_condition: NotRequired["aws_sdk_connect.types.tag_condition.TagCondition"]
    hierarchy_group_condition: NotRequired[
        "aws_sdk_connect.types.hierarchy_group_condition.HierarchyGroupCondition"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ControlPlaneUserAttributeFilter) -> dict:
    out: dict = {}
    if "or_conditions" in value:
        import aws_sdk_connect.types.attribute_or_condition_list

        out["OrConditions"] = (
            aws_sdk_connect.types.attribute_or_condition_list.serialize_json(
                value["or_conditions"]
            )
        )
    if "and_condition" in value:
        import aws_sdk_connect.types.attribute_and_condition

        out["AndCondition"] = (
            aws_sdk_connect.types.attribute_and_condition.serialize_json(
                value["and_condition"]
            )
        )
    if "tag_condition" in value:
        import aws_sdk_connect.types.tag_condition

        out["TagCondition"] = aws_sdk_connect.types.tag_condition.serialize_json(
            value["tag_condition"]
        )
    if "hierarchy_group_condition" in value:
        import aws_sdk_connect.types.hierarchy_group_condition

        out["HierarchyGroupCondition"] = (
            aws_sdk_connect.types.hierarchy_group_condition.serialize_json(
                value["hierarchy_group_condition"]
            )
        )
    return out


def deserialize_json(data: dict) -> ControlPlaneUserAttributeFilter:
    out: ControlPlaneUserAttributeFilter = {}  # type: ignore[typeddict-item]
    if "OrConditions" in data:
        import aws_sdk_connect.types.attribute_or_condition_list

        out["or_conditions"] = (
            aws_sdk_connect.types.attribute_or_condition_list.deserialize_json(
                data["OrConditions"]
            )
        )
    if "AndCondition" in data:
        import aws_sdk_connect.types.attribute_and_condition

        out["and_condition"] = (
            aws_sdk_connect.types.attribute_and_condition.deserialize_json(
                data["AndCondition"]
            )
        )
    if "TagCondition" in data:
        import aws_sdk_connect.types.tag_condition

        out["tag_condition"] = aws_sdk_connect.types.tag_condition.deserialize_json(
            data["TagCondition"]
        )
    if "HierarchyGroupCondition" in data:
        import aws_sdk_connect.types.hierarchy_group_condition

        out["hierarchy_group_condition"] = (
            aws_sdk_connect.types.hierarchy_group_condition.deserialize_json(
                data["HierarchyGroupCondition"]
            )
        )
    return out
