"""Generated from Smithy shape ``com.amazonaws.rds#DescribeDBLogFilesMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.filter_list
    import capo_rds.types.integer_optional
    import capo_rds.types.long
    import capo_rds.types.string


class DescribeDBLogFilesMessage(TypedDict, closed=True):
    db_instance_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The customer-assigned name of the DB instance that contains the log files you want to list.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing DBInstance.</p> </li> </ul>"""
    filename_contains: NotRequired["capo_rds.types.string.String"]
    """<p>Filters the available log files for log file names that contain the specified string.</p>"""
    file_last_written: NotRequired["capo_rds.types.long.Long"]
    """<p>Filters the available log files for files written since the specified date, in POSIX timestamp format with milliseconds.</p>"""
    file_size: NotRequired["capo_rds.types.long.Long"]
    """<p>Filters the available log files for files larger than the specified size.</p>"""
    filters: NotRequired["capo_rds.types.filter_list.FilterList"]
    """<p>This parameter isn't currently supported.</p>"""
    max_records: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified MaxRecords value, a pagination token called a marker is included in the response so you can retrieve the remaining results.</p>"""
    marker: NotRequired["capo_rds.types.string.String"]
    """<p>The pagination token provided in the previous request. If this parameter is specified the response includes only records beyond the marker, up to MaxRecords.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDBLogFilesMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_instance_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBInstanceIdentifier", str(value["db_instance_identifier"]))
        )
    if "filename_contains" in value:
        pairs.append((f"{key_prefix}FilenameContains", str(value["filename_contains"])))
    if "file_last_written" in value:
        pairs.append((f"{key_prefix}FileLastWritten", str(value["file_last_written"])))
    if "file_size" in value:
        pairs.append((f"{key_prefix}FileSize", str(value["file_size"])))
    if "filters" in value:
        import capo_rds.types.filter_list

        capo_rds.types.filter_list.serialize_query(
            value["filters"], pairs, f"{key_prefix}Filters"
        )
    if "max_records" in value:
        pairs.append((f"{key_prefix}MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeDBLogFilesMessage:
    out: DescribeDBLogFilesMessage = {}  # type: ignore[typeddict-item]
    child_db_instance_identifier = el.find("DBInstanceIdentifier")
    if child_db_instance_identifier is not None:
        out["db_instance_identifier"] = str(child_db_instance_identifier.text or "")
    child_filename_contains = el.find("FilenameContains")
    if child_filename_contains is not None:
        out["filename_contains"] = str(child_filename_contains.text or "")
    child_file_last_written = el.find("FileLastWritten")
    if child_file_last_written is not None:
        out["file_last_written"] = int(child_file_last_written.text or "")
    child_file_size = el.find("FileSize")
    if child_file_size is not None:
        out["file_size"] = int(child_file_size.text or "")
    child_filters = el.find("Filters")
    if child_filters is not None:
        import capo_rds.types.filter_list

        out["filters"] = capo_rds.types.filter_list.deserialize_query(child_filters)
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
