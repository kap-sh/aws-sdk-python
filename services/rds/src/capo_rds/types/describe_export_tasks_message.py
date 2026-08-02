"""Generated from Smithy shape ``com.amazonaws.rds#DescribeExportTasksMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.export_source_type
    import capo_rds.types.filter_list
    import capo_rds.types.max_records
    import capo_rds.types.string


class DescribeExportTasksMessage(TypedDict, closed=True):
    export_task_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier of the snapshot or cluster export task to be described.</p>"""
    source_arn: NotRequired["capo_rds.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the snapshot or cluster exported to Amazon S3.</p>"""
    filters: NotRequired["capo_rds.types.filter_list.FilterList"]
    """<p>Filters specify one or more snapshot or cluster exports to describe. The filters are specified as name-value pairs that define what to include in the output. Filter names and values are case-sensitive.</p> <p>Supported filters include the following:</p> <ul> <li> <p> <code>export-task-identifier</code> - An identifier for the snapshot or cluster export task.</p> </li> <li> <p> <code>s3-bucket</code> - The Amazon S3 bucket the data is exported to.</p> </li> <li> <p> <code>source-arn</code> - The Amazon Resource Name (ARN) of the snapshot or cluster exported to Amazon S3.</p> </li> <li> <p> <code>status</code> - The status of the export task. Must be lowercase. Valid statuses are the following:</p> <ul> <li> <p> <code>canceled</code> </p> </li> <li> <p> <code>canceling</code> </p> </li> <li> <p> <code>complete</code> </p> </li> <li> <p> <code>failed</code> </p> </li> <li> <p> <code>in_progress</code> </p> </li> <li> <p> <code>starting</code> </p> </li> </ul> </li> </ul>"""
    marker: NotRequired["capo_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous <code>DescribeExportTasks</code> request. If you specify this parameter, the response includes only records beyond the marker, up to the value specified by the <code>MaxRecords</code> parameter.</p>"""
    max_records: NotRequired["capo_rds.types.max_records.MaxRecords"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified value, a pagination token called a marker is included in the response. You can use the marker in a later <code>DescribeExportTasks</code> request to retrieve the remaining results.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>"""
    source_type: NotRequired["capo_rds.types.export_source_type.ExportSourceType"]
    """<p>The type of source for the export.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeExportTasksMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "export_task_identifier" in value:
        pairs.append(
            (f"{key_prefix}ExportTaskIdentifier", str(value["export_task_identifier"]))
        )
    if "source_arn" in value:
        pairs.append((f"{key_prefix}SourceArn", str(value["source_arn"])))
    if "filters" in value:
        import capo_rds.types.filter_list

        capo_rds.types.filter_list.serialize_query(
            value["filters"], pairs, f"{key_prefix}Filters"
        )
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "max_records" in value:
        pairs.append((f"{key_prefix}MaxRecords", str(value["max_records"])))
    if "source_type" in value:
        import capo_rds.types.export_source_type

        capo_rds.types.export_source_type.serialize_query(
            value["source_type"], pairs, f"{key_prefix}SourceType"
        )


def deserialize_query(el: Element) -> DescribeExportTasksMessage:
    out: DescribeExportTasksMessage = {}  # type: ignore[typeddict-item]
    child_export_task_identifier = el.find("ExportTaskIdentifier")
    if child_export_task_identifier is not None:
        out["export_task_identifier"] = str(child_export_task_identifier.text or "")
    child_source_arn = el.find("SourceArn")
    if child_source_arn is not None:
        out["source_arn"] = str(child_source_arn.text or "")
    child_filters = el.find("Filters")
    if child_filters is not None:
        import capo_rds.types.filter_list

        out["filters"] = capo_rds.types.filter_list.deserialize_query(child_filters)
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_source_type = el.find("SourceType")
    if child_source_type is not None:
        import capo_rds.types.export_source_type

        out["source_type"] = capo_rds.types.export_source_type.deserialize_query(
            child_source_type
        )
    return out
