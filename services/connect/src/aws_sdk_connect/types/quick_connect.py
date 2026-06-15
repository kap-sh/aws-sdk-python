"""Generated from Smithy shape ``com.amazonaws.connect#QuickConnect``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.quick_connect_config
    import aws_sdk_connect.types.quick_connect_description
    import aws_sdk_connect.types.quick_connect_id
    import aws_sdk_connect.types.quick_connect_name
    import aws_sdk_connect.types.region_name
    import aws_sdk_connect.types.tag_map
    import aws_sdk_connect.types.timestamp


class QuickConnect(TypedDict):
    quick_connect_arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the quick connect.</p>"""
    quick_connect_id: NotRequired[
        "aws_sdk_connect.types.quick_connect_id.QuickConnectId"
    ]
    """<p>The identifier for the quick connect.</p>"""
    name: NotRequired["aws_sdk_connect.types.quick_connect_name.QuickConnectName"]
    """<p>The name of the quick connect.</p>"""
    description: NotRequired[
        "aws_sdk_connect.types.quick_connect_description.QuickConnectDescription"
    ]
    """<p>The description.</p>"""
    quick_connect_config: NotRequired[
        "aws_sdk_connect.types.quick_connect_config.QuickConnectConfig"
    ]
    """<p>Contains information about the quick connect.</p>"""
    tags: NotRequired["aws_sdk_connect.types.tag_map.TagMap"]
    r"""<p>The tags used to organize, track, or control access for this resource. For example, { \"Tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""
    last_modified_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when this resource was last modified.</p>"""
    last_modified_region: NotRequired["aws_sdk_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where this resource was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuickConnect) -> dict:
    out: dict = {}
    if "quick_connect_arn" in value:
        out["QuickConnectARN"] = value["quick_connect_arn"]
    if "quick_connect_id" in value:
        out["QuickConnectId"] = value["quick_connect_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "quick_connect_config" in value:
        import aws_sdk_connect.types.quick_connect_config

        out["QuickConnectConfig"] = (
            aws_sdk_connect.types.quick_connect_config.serialize_json(
                value["quick_connect_config"]
            )
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


def deserialize_json(data: dict) -> QuickConnect:
    out: QuickConnect = {}  # type: ignore[typeddict-item]
    if "QuickConnectARN" in data:
        out["quick_connect_arn"] = data["QuickConnectARN"]
    if "QuickConnectId" in data:
        out["quick_connect_id"] = data["QuickConnectId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "QuickConnectConfig" in data:
        import aws_sdk_connect.types.quick_connect_config

        out["quick_connect_config"] = (
            aws_sdk_connect.types.quick_connect_config.deserialize_json(
                data["QuickConnectConfig"]
            )
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
