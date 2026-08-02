"""Generated from Smithy shape ``com.amazonaws.rds#DescribeSourceRegionsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.filter_list
    import capo_rds.types.integer_optional
    import capo_rds.types.string


class DescribeSourceRegionsMessage(TypedDict, closed=True):
    region_name: NotRequired["capo_rds.types.string.String"]
    """<p>The source Amazon Web Services Region name. For example, <code>us-east-1</code>.</p> <p>Constraints:</p> <ul> <li> <p>Must specify a valid Amazon Web Services Region name.</p> </li> </ul>"""
    max_records: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so you can retrieve the remaining results.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>"""
    marker: NotRequired["capo_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous <code>DescribeSourceRegions</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    filters: NotRequired["capo_rds.types.filter_list.FilterList"]
    """<p>This parameter isn't currently supported.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeSourceRegionsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "region_name" in value:
        pairs.append((f"{key_prefix}RegionName", str(value["region_name"])))
    if "max_records" in value:
        pairs.append((f"{key_prefix}MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "filters" in value:
        import capo_rds.types.filter_list

        capo_rds.types.filter_list.serialize_query(
            value["filters"], pairs, f"{key_prefix}Filters"
        )


def deserialize_query(el: Element) -> DescribeSourceRegionsMessage:
    out: DescribeSourceRegionsMessage = {}  # type: ignore[typeddict-item]
    child_region_name = el.find("RegionName")
    if child_region_name is not None:
        out["region_name"] = str(child_region_name.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_filters = el.find("Filters")
    if child_filters is not None:
        import capo_rds.types.filter_list

        out["filters"] = capo_rds.types.filter_list.deserialize_query(child_filters)
    return out
