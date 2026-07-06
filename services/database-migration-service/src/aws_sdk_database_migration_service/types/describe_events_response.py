"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeEventsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.event_list
    import aws_sdk_database_migration_service.types.string


class DescribeEventsResponse(TypedDict, closed=True):
    marker: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>"""
    events: NotRequired["aws_sdk_database_migration_service.types.event_list.EventList"]
    """<p>The events described.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventsResponse) -> dict:
    out: dict = {}
    if "marker" in value:
        out["Marker"] = value["marker"]
    if "events" in value:
        import aws_sdk_database_migration_service.types.event_list

        out["Events"] = (
            aws_sdk_database_migration_service.types.event_list.serialize_aws_json_1_1(
                value["events"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEventsResponse:
    out: DescribeEventsResponse = {}  # type: ignore[typeddict-item]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    if "Events" in data:
        import aws_sdk_database_migration_service.types.event_list

        out["events"] = (
            aws_sdk_database_migration_service.types.event_list.deserialize_aws_json_1_1(
                data["Events"]
            )
        )
    return out
