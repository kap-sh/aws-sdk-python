"""Generated from Smithy shape ``com.amazonaws.quicksight#Dashboard``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.dashboard_name
    import aws_sdk_quicksight.types.dashboard_version
    import aws_sdk_quicksight.types.link_entity_arn_list
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.timestamp


class Dashboard(TypedDict, closed=True):
    dashboard_id: NotRequired[
        "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>Dashboard ID.</p>"""
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    name: NotRequired["aws_sdk_quicksight.types.dashboard_name.DashboardName"]
    """<p>A display name for the dashboard.</p>"""
    version: NotRequired["aws_sdk_quicksight.types.dashboard_version.DashboardVersion"]
    """<p>Version.</p>"""
    created_time: NotRequired["aws_sdk_quicksight.types.timestamp.Timestamp"]
    """<p>The time that this dashboard was created.</p>"""
    last_published_time: NotRequired["aws_sdk_quicksight.types.timestamp.Timestamp"]
    """<p>The last time that this dashboard was published.</p>"""
    last_updated_time: NotRequired["aws_sdk_quicksight.types.timestamp.Timestamp"]
    """<p>The last time that this dashboard was updated.</p>"""
    link_entities: NotRequired[
        "aws_sdk_quicksight.types.link_entity_arn_list.LinkEntityArnList"
    ]
    """<p>A list of analysis Amazon Resource Names (ARNs) to be linked to the dashboard.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Dashboard) -> dict:
    out: dict = {}
    if "dashboard_id" in value:
        out["DashboardId"] = value["dashboard_id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "version" in value:
        import aws_sdk_quicksight.types.dashboard_version

        out["Version"] = aws_sdk_quicksight.types.dashboard_version.serialize_json(
            value["version"]
        )
    if "created_time" in value:
        import aws_sdk_quicksight.types.timestamp

        out["CreatedTime"] = aws_sdk_quicksight.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "last_published_time" in value:
        import aws_sdk_quicksight.types.timestamp

        out["LastPublishedTime"] = aws_sdk_quicksight.types.timestamp.serialize_json(
            value["last_published_time"]
        )
    if "last_updated_time" in value:
        import aws_sdk_quicksight.types.timestamp

        out["LastUpdatedTime"] = aws_sdk_quicksight.types.timestamp.serialize_json(
            value["last_updated_time"]
        )
    if "link_entities" in value:
        import aws_sdk_quicksight.types.link_entity_arn_list

        out["LinkEntities"] = (
            aws_sdk_quicksight.types.link_entity_arn_list.serialize_json(
                value["link_entities"]
            )
        )
    return out


def deserialize_json(data: dict) -> Dashboard:
    out: Dashboard = {}  # type: ignore[typeddict-item]
    if "DashboardId" in data:
        out["dashboard_id"] = data["DashboardId"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Version" in data:
        import aws_sdk_quicksight.types.dashboard_version

        out["version"] = aws_sdk_quicksight.types.dashboard_version.deserialize_json(
            data["Version"]
        )
    if "CreatedTime" in data:
        import aws_sdk_quicksight.types.timestamp

        out["created_time"] = aws_sdk_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if "LastPublishedTime" in data:
        import aws_sdk_quicksight.types.timestamp

        out["last_published_time"] = (
            aws_sdk_quicksight.types.timestamp.deserialize_json(
                data["LastPublishedTime"]
            )
        )
    if "LastUpdatedTime" in data:
        import aws_sdk_quicksight.types.timestamp

        out["last_updated_time"] = aws_sdk_quicksight.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    if "LinkEntities" in data:
        import aws_sdk_quicksight.types.link_entity_arn_list

        out["link_entities"] = (
            aws_sdk_quicksight.types.link_entity_arn_list.deserialize_json(
                data["LinkEntities"]
            )
        )
    return out
