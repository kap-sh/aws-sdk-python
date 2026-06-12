"""Generated from Smithy shape ``com.amazonaws.connect#QuickConnectSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.quick_connect_id
    import aws_sdk_connect.types.quick_connect_name
    import aws_sdk_connect.types.quick_connect_type
    import aws_sdk_connect.types.region_name
    import aws_sdk_connect.types.timestamp


class QuickConnectSummary(TypedDict):
    id: NotRequired["aws_sdk_connect.types.quick_connect_id.QuickConnectId"]
    """<p>The identifier for the quick connect.</p>"""
    arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the quick connect.</p>"""
    name: NotRequired["aws_sdk_connect.types.quick_connect_name.QuickConnectName"]
    """<p>The name of the quick connect.</p>"""
    quick_connect_type: NotRequired[
        "aws_sdk_connect.types.quick_connect_type.QuickConnectType"
    ]
    """<p>The type of quick connect. In the Connect Customer admin website, when you create a quick connect, you are prompted to assign one of the following types: Agent (USER), External (PHONE_NUMBER), or Queue (QUEUE).</p>"""
    last_modified_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when this resource was last modified.</p>"""
    last_modified_region: NotRequired["aws_sdk_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where this resource was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuickConnectSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "quick_connect_type" in value:
        import aws_sdk_connect.types.quick_connect_type

        out["QuickConnectType"] = (
            aws_sdk_connect.types.quick_connect_type.serialize_json(
                value["quick_connect_type"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_connect.types.timestamp

        out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    return out


def deserialize_json(data: dict) -> QuickConnectSummary:
    out: QuickConnectSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "QuickConnectType" in data:
        import aws_sdk_connect.types.quick_connect_type

        out["quick_connect_type"] = (
            aws_sdk_connect.types.quick_connect_type.deserialize_json(
                data["QuickConnectType"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    return out
