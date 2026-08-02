"""Generated from Smithy shape ``com.amazonaws.rds#DescribeDBMajorEngineVersionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_major_engine_versions_list
    import capo_rds.types.string


class DescribeDBMajorEngineVersionsResponse(TypedDict, closed=True):
    db_major_engine_versions: NotRequired[
        "capo_rds.types.db_major_engine_versions_list.DBMajorEngineVersionsList"
    ]
    """<p>A list of <code>DBMajorEngineVersion</code> elements.</p>"""
    marker: NotRequired["capo_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeDBMajorEngineVersionsResponse,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_major_engine_versions" in value:
        import capo_rds.types.db_major_engine_versions_list

        capo_rds.types.db_major_engine_versions_list.serialize_query(
            value["db_major_engine_versions"],
            pairs,
            f"{key_prefix}DBMajorEngineVersions",
        )
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))


def deserialize_query(el: Element) -> DescribeDBMajorEngineVersionsResponse:
    out: DescribeDBMajorEngineVersionsResponse = {}  # type: ignore[typeddict-item]
    child_db_major_engine_versions = el.find("DBMajorEngineVersions")
    if child_db_major_engine_versions is not None:
        import capo_rds.types.db_major_engine_versions_list

        out["db_major_engine_versions"] = (
            capo_rds.types.db_major_engine_versions_list.deserialize_query(
                child_db_major_engine_versions
            )
        )
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    return out
