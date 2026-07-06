"""Generated from Smithy shape ``com.amazonaws.connect#HierarchyGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.hierarchy_group_id
    import aws_sdk_connect.types.hierarchy_group_name
    import aws_sdk_connect.types.hierarchy_level_id
    import aws_sdk_connect.types.hierarchy_path
    import aws_sdk_connect.types.region_name
    import aws_sdk_connect.types.tag_map
    import aws_sdk_connect.types.timestamp


class HierarchyGroup(TypedDict, closed=True):
    id: NotRequired["aws_sdk_connect.types.hierarchy_group_id.HierarchyGroupId"]
    """<p>The identifier of the hierarchy group.</p>"""
    arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the hierarchy group.</p>"""
    name: NotRequired["aws_sdk_connect.types.hierarchy_group_name.HierarchyGroupName"]
    """<p>The name of the hierarchy group.</p>"""
    level_id: NotRequired["aws_sdk_connect.types.hierarchy_level_id.HierarchyLevelId"]
    """<p>The identifier of the level in the hierarchy group.</p>"""
    hierarchy_path: NotRequired["aws_sdk_connect.types.hierarchy_path.HierarchyPath"]
    """<p>Information about the levels in the hierarchy group.</p>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    r"""<p>The tags used to organize, track, or control access for this resource. For example, { \"Tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""
    last_modified_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when this resource was last modified.</p>"""
    last_modified_region: NotRequired["aws_sdk_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where this resource was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HierarchyGroup) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "level_id" in value:
        out["LevelId"] = value["level_id"]
    if "hierarchy_path" in value:
        import aws_sdk_connect.types.hierarchy_path

        out["HierarchyPath"] = aws_sdk_connect.types.hierarchy_path.serialize_json(
            value["hierarchy_path"]
        )
    if "tags" in value:
        import aws_sdk_connect.types.tag_map

        out["Tags"] = aws_sdk_connect.types.tag_map.serialize_json(value["tags"])
    if "last_modified_time" in value:
        import aws_sdk_connect.types.timestamp

        out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    return out


def deserialize_json(data: dict) -> HierarchyGroup:
    out: HierarchyGroup = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "LevelId" in data:
        out["level_id"] = data["LevelId"]
    if "HierarchyPath" in data:
        import aws_sdk_connect.types.hierarchy_path

        out["hierarchy_path"] = aws_sdk_connect.types.hierarchy_path.deserialize_json(
            data["HierarchyPath"]
        )
    if "Tags" in data:
        import aws_sdk_connect.types.tag_map

        out["tags"] = aws_sdk_connect.types.tag_map.deserialize_json(data["Tags"])
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    return out
