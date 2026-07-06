"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#DescribeEventsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.event_categories_list
    import aws_sdk_database_migration_service.types.filter_list
    import aws_sdk_database_migration_service.types.integer_optional
    import aws_sdk_database_migration_service.types.source_type
    import aws_sdk_database_migration_service.types.string
    import aws_sdk_database_migration_service.types.t_stamp


class DescribeEventsMessage(TypedDict, closed=True):
    source_identifier: NotRequired[
        "aws_sdk_database_migration_service.types.string.String"
    ]
    """<p> The identifier of an event source.</p>"""
    source_type: NotRequired[
        "aws_sdk_database_migration_service.types.source_type.SourceType"
    ]
    """<p>The type of DMS resource that generates events.</p> <p>Valid values: replication-instance | replication-task</p>"""
    start_time: NotRequired["aws_sdk_database_migration_service.types.t_stamp.TStamp"]
    """<p>The start time for the events to be listed.</p>"""
    end_time: NotRequired["aws_sdk_database_migration_service.types.t_stamp.TStamp"]
    """<p>The end time for the events to be listed.</p>"""
    duration: NotRequired[
        "aws_sdk_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p>The duration of the events to be listed.</p>"""
    event_categories: NotRequired[
        "aws_sdk_database_migration_service.types.event_categories_list.EventCategoriesList"
    ]
    """<p>A list of event categories for the source type that you've chosen.</p>"""
    filters: NotRequired[
        "aws_sdk_database_migration_service.types.filter_list.FilterList"
    ]
    """<p>Filters applied to events. The only valid filter is <code>replication-instance-id</code>.</p>"""
    max_records: NotRequired[
        "aws_sdk_database_migration_service.types.integer_optional.IntegerOptional"
    ]
    """<p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. </p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>"""
    marker: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventsMessage) -> dict:
    out: dict = {}
    if "source_identifier" in value:
        out["SourceIdentifier"] = value["source_identifier"]
    if "source_type" in value:
        import aws_sdk_database_migration_service.types.source_type

        out["SourceType"] = (
            aws_sdk_database_migration_service.types.source_type.serialize_aws_json_1_1(
                value["source_type"]
            )
        )
    if "start_time" in value:
        import aws_sdk_database_migration_service.types.t_stamp

        out["StartTime"] = (
            aws_sdk_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["start_time"]
            )
        )
    if "end_time" in value:
        import aws_sdk_database_migration_service.types.t_stamp

        out["EndTime"] = (
            aws_sdk_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["end_time"]
            )
        )
    if "duration" in value:
        out["Duration"] = value["duration"]
    if "event_categories" in value:
        import aws_sdk_database_migration_service.types.event_categories_list

        out["EventCategories"] = (
            aws_sdk_database_migration_service.types.event_categories_list.serialize_aws_json_1_1(
                value["event_categories"]
            )
        )
    if "filters" in value:
        import aws_sdk_database_migration_service.types.filter_list

        out["Filters"] = (
            aws_sdk_database_migration_service.types.filter_list.serialize_aws_json_1_1(
                value["filters"]
            )
        )
    if "max_records" in value:
        out["MaxRecords"] = value["max_records"]
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEventsMessage:
    out: DescribeEventsMessage = {}  # type: ignore[typeddict-item]
    if "SourceIdentifier" in data:
        out["source_identifier"] = data["SourceIdentifier"]
    if "SourceType" in data:
        import aws_sdk_database_migration_service.types.source_type

        out["source_type"] = (
            aws_sdk_database_migration_service.types.source_type.deserialize_aws_json_1_1(
                data["SourceType"]
            )
        )
    if "StartTime" in data:
        import aws_sdk_database_migration_service.types.t_stamp

        out["start_time"] = (
            aws_sdk_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["StartTime"]
            )
        )
    if "EndTime" in data:
        import aws_sdk_database_migration_service.types.t_stamp

        out["end_time"] = (
            aws_sdk_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["EndTime"]
            )
        )
    if "Duration" in data:
        out["duration"] = data["Duration"]
    if "EventCategories" in data:
        import aws_sdk_database_migration_service.types.event_categories_list

        out["event_categories"] = (
            aws_sdk_database_migration_service.types.event_categories_list.deserialize_aws_json_1_1(
                data["EventCategories"]
            )
        )
    if "Filters" in data:
        import aws_sdk_database_migration_service.types.filter_list

        out["filters"] = (
            aws_sdk_database_migration_service.types.filter_list.deserialize_aws_json_1_1(
                data["Filters"]
            )
        )
    if "MaxRecords" in data:
        out["max_records"] = data["MaxRecords"]
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
