"""Generated from Smithy shape ``com.amazonaws.docdb#DescribeEngineDefaultClusterParametersMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.filter_list
    import capo_docdb.types.integer_optional
    import capo_docdb.types.string


class DescribeEngineDefaultClusterParametersMessage(TypedDict, closed=True):
    db_parameter_group_family: NotRequired["capo_docdb.types.string.String"]
    """<p>The name of the cluster parameter group family to return the engine parameter information for.</p>"""
    filters: NotRequired["capo_docdb.types.filter_list.FilterList"]
    """<p>This parameter is not currently supported.</p>"""
    max_records: NotRequired["capo_docdb.types.integer_optional.IntegerOptional"]
    """<p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token (marker) is included in the response so that the remaining results can be retrieved.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>"""
    marker: NotRequired["capo_docdb.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeEngineDefaultClusterParametersMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "db_parameter_group_family" in value:
        pairs.append(
            (
                f"{prefix}.DBParameterGroupFamily",
                str(value["db_parameter_group_family"]),
            )
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


def deserialize_query(el: Element) -> DescribeEngineDefaultClusterParametersMessage:
    out: DescribeEngineDefaultClusterParametersMessage = {}  # type: ignore[typeddict-item]
    child_db_parameter_group_family = el.find("DBParameterGroupFamily")
    if child_db_parameter_group_family is not None:
        out["db_parameter_group_family"] = str(
            child_db_parameter_group_family.text or ""
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
