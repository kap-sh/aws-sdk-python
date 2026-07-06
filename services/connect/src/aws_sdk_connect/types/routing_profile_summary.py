"""Generated from Smithy shape ``com.amazonaws.connect#RoutingProfileSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.arn
    import aws_sdk_connect.types.region_name
    import aws_sdk_connect.types.routing_profile_id
    import aws_sdk_connect.types.routing_profile_name
    import aws_sdk_connect.types.timestamp


class RoutingProfileSummary(TypedDict, closed=True):
    id: NotRequired["aws_sdk_connect.types.routing_profile_id.RoutingProfileId"]
    """<p>The identifier of the routing profile.</p>"""
    arn: NotRequired["aws_sdk_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the routing profile.</p>"""
    name: NotRequired["aws_sdk_connect.types.routing_profile_name.RoutingProfileName"]
    """<p>The name of the routing profile.</p>"""
    last_modified_time: NotRequired["aws_sdk_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when this resource was last modified.</p>"""
    last_modified_region: NotRequired["aws_sdk_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where this resource was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoutingProfileSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "last_modified_time" in value:
        import aws_sdk_connect.types.timestamp

        out["LastModifiedTime"] = aws_sdk_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    return out


def deserialize_json(data: dict) -> RoutingProfileSummary:
    out: RoutingProfileSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "LastModifiedTime" in data:
        import aws_sdk_connect.types.timestamp

        out["last_modified_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    return out
