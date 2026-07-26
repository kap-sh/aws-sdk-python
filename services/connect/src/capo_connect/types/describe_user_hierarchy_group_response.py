"""Generated from Smithy shape ``com.amazonaws.connect#DescribeUserHierarchyGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.hierarchy_group


class DescribeUserHierarchyGroupResponse(TypedDict, closed=True):
    hierarchy_group: NotRequired["capo_connect.types.hierarchy_group.HierarchyGroup"]
    """<p>Information about the hierarchy group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeUserHierarchyGroupResponse) -> dict:
    out: dict = {}
    if "hierarchy_group" in value:
        import capo_connect.types.hierarchy_group

        out["HierarchyGroup"] = capo_connect.types.hierarchy_group.serialize_json(
            value["hierarchy_group"]
        )
    return out


def deserialize_json(data: dict) -> DescribeUserHierarchyGroupResponse:
    out: DescribeUserHierarchyGroupResponse = {}  # type: ignore[typeddict-item]
    if "HierarchyGroup" in data:
        import capo_connect.types.hierarchy_group

        out["hierarchy_group"] = capo_connect.types.hierarchy_group.deserialize_json(
            data["HierarchyGroup"]
        )
    return out
