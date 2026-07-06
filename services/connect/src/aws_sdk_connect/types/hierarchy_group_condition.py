"""Generated from Smithy shape ``com.amazonaws.connect#HierarchyGroupCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.hierarchy_group_match_type
    import aws_sdk_connect.types.string


class HierarchyGroupCondition(TypedDict, closed=True):
    value: NotRequired["aws_sdk_connect.types.string.String"]
    """<p>The value in the hierarchy group condition.</p>"""
    hierarchy_group_match_type: NotRequired[
        "aws_sdk_connect.types.hierarchy_group_match_type.HierarchyGroupMatchType"
    ]
    """<p>The type of hierarchy group match.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HierarchyGroupCondition) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    if "hierarchy_group_match_type" in value:
        import aws_sdk_connect.types.hierarchy_group_match_type

        out["HierarchyGroupMatchType"] = (
            aws_sdk_connect.types.hierarchy_group_match_type.serialize_json(
                value["hierarchy_group_match_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> HierarchyGroupCondition:
    out: HierarchyGroupCondition = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    if "HierarchyGroupMatchType" in data:
        import aws_sdk_connect.types.hierarchy_group_match_type

        out["hierarchy_group_match_type"] = (
            aws_sdk_connect.types.hierarchy_group_match_type.deserialize_json(
                data["HierarchyGroupMatchType"]
            )
        )
    return out
