"""Generated from Smithy shape ``com.amazonaws.quicksight#DashboardSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.arn
    import aws_sdk_quicksight.types.dashboard_name
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.timestamp
    import aws_sdk_quicksight.types.version_number


class DashboardSummary(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the resource.</p>"""
    dashboard_id: NotRequired[
        "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    ]
    """<p>Dashboard ID.</p>"""
    name: NotRequired["aws_sdk_quicksight.types.dashboard_name.DashboardName"]
    """<p>A display name for the dashboard.</p>"""
    created_time: NotRequired["aws_sdk_quicksight.types.timestamp.Timestamp"]
    """<p>The time that this dashboard was created.</p>"""
    last_updated_time: NotRequired["aws_sdk_quicksight.types.timestamp.Timestamp"]
    """<p>The last time that this dashboard was updated.</p>"""
    published_version_number: NotRequired[
        "aws_sdk_quicksight.types.version_number.VersionNumber"
    ]
    """<p>Published version number.</p>"""
    last_published_time: NotRequired["aws_sdk_quicksight.types.timestamp.Timestamp"]
    """<p>The last time that this dashboard was published.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DashboardSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "dashboard_id" in value:
        out["DashboardId"] = value["dashboard_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "created_time" in value:
        import aws_sdk_quicksight.types.timestamp

        out["CreatedTime"] = aws_sdk_quicksight.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "last_updated_time" in value:
        import aws_sdk_quicksight.types.timestamp

        out["LastUpdatedTime"] = aws_sdk_quicksight.types.timestamp.serialize_json(
            value["last_updated_time"]
        )
    if "published_version_number" in value:
        out["PublishedVersionNumber"] = value["published_version_number"]
    if "last_published_time" in value:
        import aws_sdk_quicksight.types.timestamp

        out["LastPublishedTime"] = aws_sdk_quicksight.types.timestamp.serialize_json(
            value["last_published_time"]
        )
    return out


def deserialize_json(data: dict) -> DashboardSummary:
    out: DashboardSummary = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "DashboardId" in data:
        out["dashboard_id"] = data["DashboardId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "CreatedTime" in data:
        import aws_sdk_quicksight.types.timestamp

        out["created_time"] = aws_sdk_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if "LastUpdatedTime" in data:
        import aws_sdk_quicksight.types.timestamp

        out["last_updated_time"] = aws_sdk_quicksight.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    if "PublishedVersionNumber" in data:
        out["published_version_number"] = data["PublishedVersionNumber"]
    if "LastPublishedTime" in data:
        import aws_sdk_quicksight.types.timestamp

        out["last_published_time"] = (
            aws_sdk_quicksight.types.timestamp.deserialize_json(
                data["LastPublishedTime"]
            )
        )
    return out
