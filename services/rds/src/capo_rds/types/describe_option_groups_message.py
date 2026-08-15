"""Generated from Smithy shape ``com.amazonaws.rds#DescribeOptionGroupsMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.filter_list
    import capo_rds.types.integer_optional
    import capo_rds.types.string


class DescribeOptionGroupsMessage(TypedDict, closed=True):
    option_group_name: NotRequired["capo_rds.types.string.String"]
    """<p>The name of the option group to describe. Can't be supplied together with EngineName or MajorEngineVersion.</p>"""
    filters: NotRequired["capo_rds.types.filter_list.FilterList"]
    """<p>This parameter isn't currently supported.</p>"""
    marker: NotRequired["capo_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous DescribeOptionGroups request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    max_records: NotRequired["capo_rds.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that you can retrieve the remaining results.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>"""
    engine_name: NotRequired["capo_rds.types.string.String"]
    """<p>A filter to only include option groups associated with this database engine.</p> <p>Valid Values:</p> <ul> <li> <p> <code>db2-ae</code> </p> </li> <li> <p> <code>db2-ce</code> </p> </li> <li> <p> <code>db2-se</code> </p> </li> <li> <p> <code>mariadb</code> </p> </li> <li> <p> <code>mysql</code> </p> </li> <li> <p> <code>oracle-ee</code> </p> </li> <li> <p> <code>oracle-ee-cdb</code> </p> </li> <li> <p> <code>oracle-se2</code> </p> </li> <li> <p> <code>oracle-se2-cdb</code> </p> </li> <li> <p> <code>postgres</code> </p> </li> <li> <p> <code>sqlserver-ee</code> </p> </li> <li> <p> <code>sqlserver-se</code> </p> </li> <li> <p> <code>sqlserver-ex</code> </p> </li> <li> <p> <code>sqlserver-web</code> </p> </li> </ul>"""
    major_engine_version: NotRequired["capo_rds.types.string.String"]
    """<p>Filters the list of option groups to only include groups associated with a specific database engine version. If specified, then EngineName must also be specified.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeOptionGroupsMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "option_group_name" in value:
        pairs.append((f"{key_prefix}OptionGroupName", str(value["option_group_name"])))
    if "filters" in value:
        import capo_rds.types.filter_list

        capo_rds.types.filter_list.serialize_query(
            value["filters"], pairs, f"{key_prefix}Filters"
        )
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "max_records" in value:
        pairs.append((f"{key_prefix}MaxRecords", str(value["max_records"])))
    if "engine_name" in value:
        pairs.append((f"{key_prefix}EngineName", str(value["engine_name"])))
    if "major_engine_version" in value:
        pairs.append(
            (f"{key_prefix}MajorEngineVersion", str(value["major_engine_version"]))
        )


def deserialize_query(el: Element) -> DescribeOptionGroupsMessage:
    out: DescribeOptionGroupsMessage = {}  # type: ignore[typeddict-item]
    child_option_group_name = el.find("OptionGroupName")
    if child_option_group_name is not None:
        out["option_group_name"] = str(child_option_group_name.text or "")
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
    child_engine_name = el.find("EngineName")
    if child_engine_name is not None:
        out["engine_name"] = str(child_engine_name.text or "")
    child_major_engine_version = el.find("MajorEngineVersion")
    if child_major_engine_version is not None:
        out["major_engine_version"] = str(child_major_engine_version.text or "")
    return out
