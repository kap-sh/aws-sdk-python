"""Generated from Smithy shape ``com.amazonaws.docdb#DescribePendingMaintenanceActionsMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_docdb.types.filter_list
    import aws_sdk_docdb.types.integer_optional
    import aws_sdk_docdb.types.string


class DescribePendingMaintenanceActionsMessage(TypedDict):
    resource_identifier: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>The ARN of a resource to return pending maintenance actions for.</p>"""
    filters: NotRequired["aws_sdk_docdb.types.filter_list.FilterList"]
    """<p>A filter that specifies one or more resources to return pending maintenance actions for.</p> <p>Supported filters:</p> <ul> <li> <p> <code>db-cluster-id</code> - Accepts cluster identifiers and cluster Amazon Resource Names (ARNs). The results list includes only pending maintenance actions for the clusters identified by these ARNs.</p> </li> <li> <p> <code>db-instance-id</code> - Accepts instance identifiers and instance ARNs. The results list includes only pending maintenance actions for the DB instances identified by these ARNs.</p> </li> </ul>"""
    marker: NotRequired["aws_sdk_docdb.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    max_records: NotRequired["aws_sdk_docdb.types.integer_optional.IntegerOptional"]
    """<p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribePendingMaintenanceActionsMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "resource_identifier" in value:
        pairs.append(
            (f"{prefix}.ResourceIdentifier", str(value["resource_identifier"]))
        )
    if "filters" in value:
        import aws_sdk_docdb.types.filter_list

        aws_sdk_docdb.types.filter_list.serialize_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))


def deserialize_query(el: Element) -> DescribePendingMaintenanceActionsMessage:
    out: DescribePendingMaintenanceActionsMessage = {}  # type: ignore[typeddict-item]
    child_resource_identifier = el.find("ResourceIdentifier")
    if child_resource_identifier is not None:
        out["resource_identifier"] = str(child_resource_identifier.text or "")
    child_filters = el.find("Filters")
    if child_filters is not None:
        import aws_sdk_docdb.types.filter_list

        out["filters"] = aws_sdk_docdb.types.filter_list.deserialize_query(
            child_filters
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    return out
