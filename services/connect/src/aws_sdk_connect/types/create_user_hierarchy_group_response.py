"""Generated from Smithy shape ``com.amazonaws.connect#CreateUserHierarchyGroupResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.hierarchy_group_id


class CreateUserHierarchyGroupResponse(TypedDict):
    hierarchy_group_id: NotRequired[
        "aws_sdk_connect.types.hierarchy_group_id.HierarchyGroupId"
    ]
    """<p>The identifier of the hierarchy group.</p>"""
    hierarchy_group_arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the hierarchy group. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateUserHierarchyGroupResponse) -> dict:
    out: dict = {}
    if "hierarchy_group_id" in value:
        out["HierarchyGroupId"] = value["hierarchy_group_id"]
    if "hierarchy_group_arn" in value:
        out["HierarchyGroupArn"] = value["hierarchy_group_arn"]
    return out


def deserialize_json(data: dict) -> CreateUserHierarchyGroupResponse:
    out: CreateUserHierarchyGroupResponse = {}  # type: ignore[typeddict-item]
    if "HierarchyGroupId" in data:
        out["hierarchy_group_id"] = data["HierarchyGroupId"]
    if "HierarchyGroupArn" in data:
        out["hierarchy_group_arn"] = data["HierarchyGroupArn"]
    return out
