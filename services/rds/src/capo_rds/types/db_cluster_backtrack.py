"""Generated from Smithy shape ``com.amazonaws.rds#DBClusterBacktrack``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string
    import capo_rds.types.t_stamp


class DBClusterBacktrack(TypedDict, closed=True):
    db_cluster_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>Contains a user-supplied DB cluster identifier. This identifier is the unique key that identifies a DB cluster.</p>"""
    backtrack_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>Contains the backtrack identifier.</p>"""
    backtrack_to: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The timestamp of the time to which the DB cluster was backtracked.</p>"""
    backtracked_from: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The timestamp of the time from which the DB cluster was backtracked.</p>"""
    backtrack_request_creation_time: NotRequired["capo_rds.types.t_stamp.TStamp"]
    """<p>The timestamp of the time at which the backtrack was requested.</p>"""
    status: NotRequired["capo_rds.types.string.String"]
    """<p>The status of the backtrack. This property returns one of the following values:</p> <ul> <li> <p> <code>applying</code> - The backtrack is currently being applied to or rolled back from the DB cluster.</p> </li> <li> <p> <code>completed</code> - The backtrack has successfully been applied to or rolled back from the DB cluster.</p> </li> <li> <p> <code>failed</code> - An error occurred while the backtrack was applied to or rolled back from the DB cluster.</p> </li> <li> <p> <code>pending</code> - The backtrack is currently pending application to or rollback from the DB cluster.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterBacktrack, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )
    if "backtrack_identifier" in value:
        pairs.append(
            (f"{key_prefix}BacktrackIdentifier", str(value["backtrack_identifier"]))
        )
    if "backtrack_to" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["backtrack_to"], pairs, f"{key_prefix}BacktrackTo"
        )
    if "backtracked_from" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["backtracked_from"], pairs, f"{key_prefix}BacktrackedFrom"
        )
    if "backtrack_request_creation_time" in value:
        import capo_rds.types.t_stamp

        capo_rds.types.t_stamp.serialize_query(
            value["backtrack_request_creation_time"],
            pairs,
            f"{key_prefix}BacktrackRequestCreationTime",
        )
    if "status" in value:
        pairs.append((f"{key_prefix}Status", str(value["status"])))


def deserialize_query(el: Element) -> DBClusterBacktrack:
    out: DBClusterBacktrack = {}  # type: ignore[typeddict-item]
    child_db_cluster_identifier = el.find("DBClusterIdentifier")
    if child_db_cluster_identifier is not None:
        out["db_cluster_identifier"] = str(child_db_cluster_identifier.text or "")
    child_backtrack_identifier = el.find("BacktrackIdentifier")
    if child_backtrack_identifier is not None:
        out["backtrack_identifier"] = str(child_backtrack_identifier.text or "")
    child_backtrack_to = el.find("BacktrackTo")
    if child_backtrack_to is not None:
        import capo_rds.types.t_stamp

        out["backtrack_to"] = capo_rds.types.t_stamp.deserialize_query(
            child_backtrack_to
        )
    child_backtracked_from = el.find("BacktrackedFrom")
    if child_backtracked_from is not None:
        import capo_rds.types.t_stamp

        out["backtracked_from"] = capo_rds.types.t_stamp.deserialize_query(
            child_backtracked_from
        )
    child_backtrack_request_creation_time = el.find("BacktrackRequestCreationTime")
    if child_backtrack_request_creation_time is not None:
        import capo_rds.types.t_stamp

        out["backtrack_request_creation_time"] = (
            capo_rds.types.t_stamp.deserialize_query(
                child_backtrack_request_creation_time
            )
        )
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    return out
