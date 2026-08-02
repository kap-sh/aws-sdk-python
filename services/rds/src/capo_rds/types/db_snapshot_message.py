"""Generated from Smithy shape ``com.amazonaws.rds#DBSnapshotMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_snapshot_list
    import capo_rds.types.string


class DBSnapshotMessage(TypedDict, closed=True):
    marker: NotRequired["capo_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    db_snapshots: NotRequired["capo_rds.types.db_snapshot_list.DBSnapshotList"]
    """<p>A list of <code>DBSnapshot</code> instances.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBSnapshotMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "db_snapshots" in value:
        import capo_rds.types.db_snapshot_list

        capo_rds.types.db_snapshot_list.serialize_query(
            value["db_snapshots"], pairs, f"{key_prefix}DBSnapshots"
        )


def deserialize_query(el: Element) -> DBSnapshotMessage:
    out: DBSnapshotMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_db_snapshots = el.find("DBSnapshots")
    if child_db_snapshots is not None:
        import capo_rds.types.db_snapshot_list

        out["db_snapshots"] = capo_rds.types.db_snapshot_list.deserialize_query(
            child_db_snapshots
        )
    return out
