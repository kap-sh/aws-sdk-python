"""Generated from Smithy shape ``com.amazonaws.neptune#DBEngineVersionMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.db_engine_version_list
    import aws_sdk_neptune.types.string


class DBEngineVersionMessage(TypedDict, closed=True):
    marker: NotRequired["aws_sdk_neptune.types.string.String"]
    """<p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    db_engine_versions: NotRequired[
        "aws_sdk_neptune.types.db_engine_version_list.DBEngineVersionList"
    ]
    """<p> A list of <code>DBEngineVersion</code> elements.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBEngineVersionMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "marker" in value:
        pairs.append((f"{prefix}.Marker", str(value["marker"])))
    if "db_engine_versions" in value:
        import aws_sdk_neptune.types.db_engine_version_list

        aws_sdk_neptune.types.db_engine_version_list.serialize_query(
            value["db_engine_versions"], pairs, f"{prefix}.DBEngineVersions"
        )


def deserialize_query(el: Element) -> DBEngineVersionMessage:
    out: DBEngineVersionMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_db_engine_versions = el.find("DBEngineVersions")
    if child_db_engine_versions is not None:
        import aws_sdk_neptune.types.db_engine_version_list

        out["db_engine_versions"] = (
            aws_sdk_neptune.types.db_engine_version_list.deserialize_query(
                child_db_engine_versions
            )
        )
    return out
