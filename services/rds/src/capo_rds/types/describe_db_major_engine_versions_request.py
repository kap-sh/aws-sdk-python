"""Generated from Smithy shape ``com.amazonaws.rds#DescribeDBMajorEngineVersionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.engine
    import capo_rds.types.major_engine_version
    import capo_rds.types.marker
    import capo_rds.types.max_records


class DescribeDBMajorEngineVersionsRequest(TypedDict, closed=True):
    engine: NotRequired["capo_rds.types.engine.Engine"]
    """<p>The database engine to return major version details for.</p> <p>Valid Values:</p> <ul> <li> <p> <code>aurora-mysql</code> </p> </li> <li> <p> <code>aurora-postgresql</code> </p> </li> <li> <p> <code>custom-sqlserver-ee</code> </p> </li> <li> <p> <code>custom-sqlserver-se</code> </p> </li> <li> <p> <code>custom-sqlserver-web</code> </p> </li> <li> <p> <code>db2-ae</code> </p> </li> <li> <p> <code>db2-se</code> </p> </li> <li> <p> <code>mariadb</code> </p> </li> <li> <p> <code>mysql</code> </p> </li> <li> <p> <code>oracle-ee</code> </p> </li> <li> <p> <code>oracle-ee-cdb</code> </p> </li> <li> <p> <code>oracle-se2</code> </p> </li> <li> <p> <code>oracle-se2-cdb</code> </p> </li> <li> <p> <code>postgres</code> </p> </li> <li> <p> <code>sqlserver-ee</code> </p> </li> <li> <p> <code>sqlserver-se</code> </p> </li> <li> <p> <code>sqlserver-ex</code> </p> </li> <li> <p> <code>sqlserver-web</code> </p> </li> </ul>"""
    major_engine_version: NotRequired[
        "capo_rds.types.major_engine_version.MajorEngineVersion"
    ]
    """<p>A specific database major engine version to return details for.</p> <p>Example: <code>8.4</code> </p>"""
    marker: NotRequired["capo_rds.types.marker.Marker"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    max_records: NotRequired["capo_rds.types.max_records.MaxRecords"]
    """<p>The maximum number of records to include in the response. If more than the <code>MaxRecords</code> value is available, a pagination token called a marker is included in the response so you can retrieve the remaining results.</p> <p>Default: 100</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDBMajorEngineVersionsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "engine" in value:
        pairs.append((f"{prefix}.Engine", str(value["engine"])))
    if "major_engine_version" in value:
        pairs.append(
            (f"{prefix}.MajorEngineVersion", str(value["major_engine_version"]))
        )
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))


def deserialize_query(el: Element) -> DescribeDBMajorEngineVersionsRequest:
    out: DescribeDBMajorEngineVersionsRequest = {}  # type: ignore[typeddict-item]
    child_engine = el.find("Engine")
    if child_engine is not None:
        out["engine"] = str(child_engine.text or "")
    child_major_engine_version = el.find("MajorEngineVersion")
    if child_major_engine_version is not None:
        out["major_engine_version"] = str(child_major_engine_version.text or "")
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    return out
