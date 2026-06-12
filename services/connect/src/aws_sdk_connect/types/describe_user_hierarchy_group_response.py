"""Generated from Smithy shape ``com.amazonaws.connect#DescribeUserHierarchyGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.hierarchy_group


class DescribeUserHierarchyGroupResponse(TypedDict):
    hierarchy_group: NotRequired["aws_sdk_connect.types.hierarchy_group.HierarchyGroup"]
    """<p>Information about the hierarchy group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeUserHierarchyGroupResponse) -> dict:
    out: dict = {}
    if "hierarchy_group" in value:
        import aws_sdk_connect.types.hierarchy_group

        out["HierarchyGroup"] = aws_sdk_connect.types.hierarchy_group.serialize_json(
            value["hierarchy_group"]
        )
    return out


def deserialize_json(data: dict) -> DescribeUserHierarchyGroupResponse:
    out: DescribeUserHierarchyGroupResponse = {}  # type: ignore[typeddict-item]
    if "HierarchyGroup" in data:
        import aws_sdk_connect.types.hierarchy_group

        out["hierarchy_group"] = aws_sdk_connect.types.hierarchy_group.deserialize_json(
            data["HierarchyGroup"]
        )
    return out
