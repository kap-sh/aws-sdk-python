"""Generated from Smithy shape ``com.amazonaws.connect#AgentHierarchyGroups``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.hierarchy_group_id_list


class AgentHierarchyGroups(TypedDict, closed=True):
    l1_ids: NotRequired[
        "aws_sdk_connect.types.hierarchy_group_id_list.HierarchyGroupIdList"
    ]
    """<p>The identifiers for level 1 hierarchy groups.</p>"""
    l2_ids: NotRequired[
        "aws_sdk_connect.types.hierarchy_group_id_list.HierarchyGroupIdList"
    ]
    """<p>The identifiers for level 2 hierarchy groups.</p>"""
    l3_ids: NotRequired[
        "aws_sdk_connect.types.hierarchy_group_id_list.HierarchyGroupIdList"
    ]
    """<p>The identifiers for level 3 hierarchy groups.</p>"""
    l4_ids: NotRequired[
        "aws_sdk_connect.types.hierarchy_group_id_list.HierarchyGroupIdList"
    ]
    """<p>The identifiers for level 4 hierarchy groups.</p>"""
    l5_ids: NotRequired[
        "aws_sdk_connect.types.hierarchy_group_id_list.HierarchyGroupIdList"
    ]
    """<p>The identifiers for level 5 hierarchy groups.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentHierarchyGroups) -> dict:
    out: dict = {}
    if "l1_ids" in value:
        import aws_sdk_connect.types.hierarchy_group_id_list

        out["L1Ids"] = aws_sdk_connect.types.hierarchy_group_id_list.serialize_json(
            value["l1_ids"]
        )
    if "l2_ids" in value:
        import aws_sdk_connect.types.hierarchy_group_id_list

        out["L2Ids"] = aws_sdk_connect.types.hierarchy_group_id_list.serialize_json(
            value["l2_ids"]
        )
    if "l3_ids" in value:
        import aws_sdk_connect.types.hierarchy_group_id_list

        out["L3Ids"] = aws_sdk_connect.types.hierarchy_group_id_list.serialize_json(
            value["l3_ids"]
        )
    if "l4_ids" in value:
        import aws_sdk_connect.types.hierarchy_group_id_list

        out["L4Ids"] = aws_sdk_connect.types.hierarchy_group_id_list.serialize_json(
            value["l4_ids"]
        )
    if "l5_ids" in value:
        import aws_sdk_connect.types.hierarchy_group_id_list

        out["L5Ids"] = aws_sdk_connect.types.hierarchy_group_id_list.serialize_json(
            value["l5_ids"]
        )
    return out


def deserialize_json(data: dict) -> AgentHierarchyGroups:
    out: AgentHierarchyGroups = {}  # type: ignore[typeddict-item]
    if "L1Ids" in data:
        import aws_sdk_connect.types.hierarchy_group_id_list

        out["l1_ids"] = aws_sdk_connect.types.hierarchy_group_id_list.deserialize_json(
            data["L1Ids"]
        )
    if "L2Ids" in data:
        import aws_sdk_connect.types.hierarchy_group_id_list

        out["l2_ids"] = aws_sdk_connect.types.hierarchy_group_id_list.deserialize_json(
            data["L2Ids"]
        )
    if "L3Ids" in data:
        import aws_sdk_connect.types.hierarchy_group_id_list

        out["l3_ids"] = aws_sdk_connect.types.hierarchy_group_id_list.deserialize_json(
            data["L3Ids"]
        )
    if "L4Ids" in data:
        import aws_sdk_connect.types.hierarchy_group_id_list

        out["l4_ids"] = aws_sdk_connect.types.hierarchy_group_id_list.deserialize_json(
            data["L4Ids"]
        )
    if "L5Ids" in data:
        import aws_sdk_connect.types.hierarchy_group_id_list

        out["l5_ids"] = aws_sdk_connect.types.hierarchy_group_id_list.deserialize_json(
            data["L5Ids"]
        )
    return out
