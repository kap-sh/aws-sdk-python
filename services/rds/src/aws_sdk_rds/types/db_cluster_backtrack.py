"""Generated from Smithy shape ``com.amazonaws.rds#DBClusterBacktrack``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.string
    import aws_sdk_rds.types.t_stamp


class DBClusterBacktrack(TypedDict):
    db_cluster_identifier: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>Contains a user-supplied DB cluster identifier. This identifier is the unique key that identifies a DB cluster.</p>"""
    backtrack_identifier: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>Contains the backtrack identifier.</p>"""
    backtrack_to: NotRequired["aws_sdk_rds.types.t_stamp.TStamp"]
    """<p>The timestamp of the time to which the DB cluster was backtracked.</p>"""
    backtracked_from: NotRequired["aws_sdk_rds.types.t_stamp.TStamp"]
    """<p>The timestamp of the time from which the DB cluster was backtracked.</p>"""
    backtrack_request_creation_time: NotRequired["aws_sdk_rds.types.t_stamp.TStamp"]
    """<p>The timestamp of the time at which the backtrack was requested.</p>"""
    status: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The status of the backtrack. This property returns one of the following values:</p> <ul> <li> <p> <code>applying</code> - The backtrack is currently being applied to or rolled back from the DB cluster.</p> </li> <li> <p> <code>completed</code> - The backtrack has successfully been applied to or rolled back from the DB cluster.</p> </li> <li> <p> <code>failed</code> - An error occurred while the backtrack was applied to or rolled back from the DB cluster.</p> </li> <li> <p> <code>pending</code> - The backtrack is currently pending application to or rollback from the DB cluster.</p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterBacktrack, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{prefix}.DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )
    if "backtrack_identifier" in value:
        pairs.append(
            (f"{prefix}.BacktrackIdentifier", str(value["backtrack_identifier"]))
        )
    if "backtrack_to" in value:
        import aws_sdk_rds.types.t_stamp

        aws_sdk_rds.types.t_stamp.serialize_query(
            value["backtrack_to"], pairs, f"{prefix}.BacktrackTo"
        )
    if "backtracked_from" in value:
        import aws_sdk_rds.types.t_stamp

        aws_sdk_rds.types.t_stamp.serialize_query(
            value["backtracked_from"], pairs, f"{prefix}.BacktrackedFrom"
        )
    if "backtrack_request_creation_time" in value:
        import aws_sdk_rds.types.t_stamp

        aws_sdk_rds.types.t_stamp.serialize_query(
            value["backtrack_request_creation_time"],
            pairs,
            f"{prefix}.BacktrackRequestCreationTime",
        )
    if "status" in value:
        pairs.append((f"{prefix}.Status", str(value["status"])))


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
        import aws_sdk_rds.types.t_stamp

        out["backtrack_to"] = aws_sdk_rds.types.t_stamp.deserialize_query(
            child_backtrack_to
        )
    child_backtracked_from = el.find("BacktrackedFrom")
    if child_backtracked_from is not None:
        import aws_sdk_rds.types.t_stamp

        out["backtracked_from"] = aws_sdk_rds.types.t_stamp.deserialize_query(
            child_backtracked_from
        )
    child_backtrack_request_creation_time = el.find("BacktrackRequestCreationTime")
    if child_backtrack_request_creation_time is not None:
        import aws_sdk_rds.types.t_stamp

        out["backtrack_request_creation_time"] = (
            aws_sdk_rds.types.t_stamp.deserialize_query(
                child_backtrack_request_creation_time
            )
        )
    child_status = el.find("Status")
    if child_status is not None:
        out["status"] = str(child_status.text or "")
    return out
