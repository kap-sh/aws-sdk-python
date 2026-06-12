"""Generated from Smithy shape ``com.amazonaws.rds#DescribeEngineDefaultParametersMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.filter_list
    import aws_sdk_rds.types.integer_optional
    import aws_sdk_rds.types.string


class DescribeEngineDefaultParametersMessage(TypedDict):
    db_parameter_group_family: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The name of the DB parameter group family.</p> <p>Valid Values:</p> <ul> <li> <p> <code>aurora-mysql5.7</code> </p> </li> <li> <p> <code>aurora-mysql8.0</code> </p> </li> <li> <p> <code>aurora-postgresql10</code> </p> </li> <li> <p> <code>aurora-postgresql11</code> </p> </li> <li> <p> <code>aurora-postgresql12</code> </p> </li> <li> <p> <code>aurora-postgresql13</code> </p> </li> <li> <p> <code>aurora-postgresql14</code> </p> </li> <li> <p> <code>custom-oracle-ee-19</code> </p> </li> <li> <p> <code>custom-oracle-ee-cdb-19</code> </p> </li> <li> <p> <code>db2-ae</code> </p> </li> <li> <p> <code>db2-se</code> </p> </li> <li> <p> <code>mariadb10.2</code> </p> </li> <li> <p> <code>mariadb10.3</code> </p> </li> <li> <p> <code>mariadb10.4</code> </p> </li> <li> <p> <code>mariadb10.5</code> </p> </li> <li> <p> <code>mariadb10.6</code> </p> </li> <li> <p> <code>mysql5.7</code> </p> </li> <li> <p> <code>mysql8.0</code> </p> </li> <li> <p> <code>oracle-ee-19</code> </p> </li> <li> <p> <code>oracle-ee-cdb-19</code> </p> </li> <li> <p> <code>oracle-ee-cdb-21</code> </p> </li> <li> <p> <code>oracle-se2-19</code> </p> </li> <li> <p> <code>oracle-se2-cdb-19</code> </p> </li> <li> <p> <code>oracle-se2-cdb-21</code> </p> </li> <li> <p> <code>postgres10</code> </p> </li> <li> <p> <code>postgres11</code> </p> </li> <li> <p> <code>postgres12</code> </p> </li> <li> <p> <code>postgres13</code> </p> </li> <li> <p> <code>postgres14</code> </p> </li> <li> <p> <code>sqlserver-ee-11.0</code> </p> </li> <li> <p> <code>sqlserver-ee-12.0</code> </p> </li> <li> <p> <code>sqlserver-ee-13.0</code> </p> </li> <li> <p> <code>sqlserver-ee-14.0</code> </p> </li> <li> <p> <code>sqlserver-ee-15.0</code> </p> </li> <li> <p> <code>sqlserver-ex-11.0</code> </p> </li> <li> <p> <code>sqlserver-ex-12.0</code> </p> </li> <li> <p> <code>sqlserver-ex-13.0</code> </p> </li> <li> <p> <code>sqlserver-ex-14.0</code> </p> </li> <li> <p> <code>sqlserver-ex-15.0</code> </p> </li> <li> <p> <code>sqlserver-se-11.0</code> </p> </li> <li> <p> <code>sqlserver-se-12.0</code> </p> </li> <li> <p> <code>sqlserver-se-13.0</code> </p> </li> <li> <p> <code>sqlserver-se-14.0</code> </p> </li> <li> <p> <code>sqlserver-se-15.0</code> </p> </li> <li> <p> <code>sqlserver-web-11.0</code> </p> </li> <li> <p> <code>sqlserver-web-12.0</code> </p> </li> <li> <p> <code>sqlserver-web-13.0</code> </p> </li> <li> <p> <code>sqlserver-web-14.0</code> </p> </li> <li> <p> <code>sqlserver-web-15.0</code> </p> </li> </ul>"""
    filters: NotRequired["aws_sdk_rds.types.filter_list.FilterList"]
    """<p>A filter that specifies one or more parameters to describe.</p> <p>The only supported filter is <code>parameter-name</code>. The results list only includes information about the parameters with these names.</p>"""
    max_records: NotRequired["aws_sdk_rds.types.integer_optional.IntegerOptional"]
    """<p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so you can retrieve the remaining results.</p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>"""
    marker: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous <code>DescribeEngineDefaultParameters</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeEngineDefaultParametersMessage,
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
        import aws_sdk_rds.types.filter_list

        aws_sdk_rds.types.filter_list.serialize_query(
            value["filters"], pairs, f"{prefix}.Filters"
        )
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeEngineDefaultParametersMessage:
    out: DescribeEngineDefaultParametersMessage = {}  # type: ignore[typeddict-item]
    child_db_parameter_group_family = el.find("DBParameterGroupFamily")
    if child_db_parameter_group_family is not None:
        out["db_parameter_group_family"] = str(
            child_db_parameter_group_family.text or ""
        )
    child_filters = el.find("Filters")
    if child_filters is not None:
        import aws_sdk_rds.types.filter_list

        out["filters"] = aws_sdk_rds.types.filter_list.deserialize_query(child_filters)
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
