"""Generated from Smithy shape ``com.amazonaws.docdb#DescribeEventsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.event_categories_list
    import capo_docdb.types.filter_list
    import capo_docdb.types.integer_optional
    import capo_docdb.types.source_type
    import capo_docdb.types.string
    import capo_docdb.types.t_stamp


class DescribeEventsMessage(TypedDict, closed=True):
    source_identifier: NotRequired["capo_docdb.types.string.String"]
    """<p>The identifier of the event source for which events are returned. If not specified, then all sources are included in the response.</p> <p>Constraints:</p> <ul> <li> <p>If <code>SourceIdentifier</code> is provided, <code>SourceType</code> must also be provided.</p> </li> <li> <p>If the source type is <code>DBInstance</code>, a <code>DBInstanceIdentifier</code> must be provided.</p> </li> <li> <p>If the source type is <code>DBSecurityGroup</code>, a <code>DBSecurityGroupName</code> must be provided.</p> </li> <li> <p>If the source type is <code>DBParameterGroup</code>, a <code>DBParameterGroupName</code> must be provided.</p> </li> <li> <p>If the source type is <code>DBSnapshot</code>, a <code>DBSnapshotIdentifier</code> must be provided.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul>"""
    source_type: NotRequired["capo_docdb.types.source_type.SourceType"]
    """<p>The event source to retrieve events for. If no value is specified, all events are returned.</p>"""
    start_time: NotRequired["capo_docdb.types.t_stamp.TStamp"]
    """<p> The beginning of the time interval to retrieve events for, specified in ISO 8601 format. </p> <p>Example: 2009-07-08T18:00Z</p>"""
    end_time: NotRequired["capo_docdb.types.t_stamp.TStamp"]
    """<p> The end of the time interval for which to retrieve events, specified in ISO 8601 format. </p> <p>Example: 2009-07-08T18:00Z</p>"""
    duration: NotRequired["capo_docdb.types.integer_optional.IntegerOptional"]
    """<p>The number of minutes to retrieve events for.</p> <p>Default: 60</p>"""
    event_categories: NotRequired[
        "capo_docdb.types.event_categories_list.EventCategoriesList"
    ]
    """<p>A list of event categories that trigger notifications for an event notification subscription.</p>"""
    filters: NotRequired["capo_docdb.types.filter_list.FilterList"]
    """<p>This parameter is not currently supported.</p>"""
    max_records: NotRequired["capo_docdb.types.integer_optional.IntegerOptional"]
    """<p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>"""
    marker: NotRequired["capo_docdb.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeEventsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "source_identifier" in value:
        pairs.append((f"{prefix}.SourceIdentifier", str(value["source_identifier"])))
    if "source_type" in value:
        import capo_docdb.types.source_type

        capo_docdb.types.source_type.serialize_query(
            value["source_type"], pairs, f"{prefix}.SourceType"
        )
    if "start_time" in value:
        import capo_docdb.types.t_stamp

        capo_docdb.types.t_stamp.serialize_query(
            value["start_time"], pairs, f"{prefix}.StartTime"
        )
    if "end_time" in value:
        import capo_docdb.types.t_stamp

        capo_docdb.types.t_stamp.serialize_query(
            value["end_time"], pairs, f"{prefix}.EndTime"
        )
    if "duration" in value:
        pairs.append((f"{prefix}.Duration", str(value["duration"])))
    if "event_categories" in value:
        import capo_docdb.types.event_categories_list

        capo_docdb.types.event_categories_list.serialize_query(
            value["event_categories"], pairs, f"{prefix}.EventCategories"
        )
    if "filters" in value:
        import capo_docdb.types.filter_list

        capo_docdb.types.filter_list.serialize_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeEventsMessage:
    out: DescribeEventsMessage = {}  # type: ignore[typeddict-item]
    child_source_identifier = el.find("SourceIdentifier")
    if child_source_identifier is not None:
        out["source_identifier"] = str(child_source_identifier.text or "")
    child_source_type = el.find("SourceType")
    if child_source_type is not None:
        import capo_docdb.types.source_type

        out["source_type"] = capo_docdb.types.source_type.deserialize_query(
            child_source_type
        )
    child_start_time = el.find("StartTime")
    if child_start_time is not None:
        import capo_docdb.types.t_stamp

        out["start_time"] = capo_docdb.types.t_stamp.deserialize_query(child_start_time)
    child_end_time = el.find("EndTime")
    if child_end_time is not None:
        import capo_docdb.types.t_stamp

        out["end_time"] = capo_docdb.types.t_stamp.deserialize_query(child_end_time)
    child_duration = el.find("Duration")
    if child_duration is not None:
        out["duration"] = int(child_duration.text or "")
    child_event_categories = el.find("EventCategories")
    if child_event_categories is not None:
        import capo_docdb.types.event_categories_list

        out["event_categories"] = (
            capo_docdb.types.event_categories_list.deserialize_query(
                child_event_categories
            )
        )
    child_filters = el.find("Filters")
    if child_filters is not None:
        import capo_docdb.types.filter_list

        out["filters"] = capo_docdb.types.filter_list.deserialize_query(child_filters)
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
