"""Generated from Smithy shape ``com.amazonaws.connect#DescribeUserHierarchyStructureResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.hierarchy_structure


class DescribeUserHierarchyStructureResponse(TypedDict, closed=True):
    hierarchy_structure: NotRequired[
        "aws_sdk_connect.types.hierarchy_structure.HierarchyStructure"
    ]
    """<p>Information about the hierarchy structure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeUserHierarchyStructureResponse) -> dict:
    out: dict = {}
    if "hierarchy_structure" in value:
        import aws_sdk_connect.types.hierarchy_structure

        out["HierarchyStructure"] = (
            aws_sdk_connect.types.hierarchy_structure.serialize_json(
                value["hierarchy_structure"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeUserHierarchyStructureResponse:
    out: DescribeUserHierarchyStructureResponse = {}  # type: ignore[typeddict-item]
    if "HierarchyStructure" in data:
        import aws_sdk_connect.types.hierarchy_structure

        out["hierarchy_structure"] = (
            aws_sdk_connect.types.hierarchy_structure.deserialize_json(
                data["HierarchyStructure"]
            )
        )
    return out
