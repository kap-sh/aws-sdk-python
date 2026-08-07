"""Generated from Smithy shape ``com.amazonaws.neptune#FailoverDBClusterMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.string


class FailoverDBClusterMessage(TypedDict, closed=True):
    db_cluster_identifier: NotRequired["capo_neptune.types.string.String"]
    """<p>A DB cluster identifier to force a failover for. This parameter is not case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing DBCluster.</p> </li> </ul>"""
    target_db_instance_identifier: NotRequired["capo_neptune.types.string.String"]
    """<p>The name of the instance to promote to the primary instance.</p> <p>You must specify the instance identifier for an Read Replica in the DB cluster. For example, <code>mydbcluster-replica1</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: FailoverDBClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )
    if "target_db_instance_identifier" in value:
        pairs.append(
            (
                f"{key_prefix}TargetDBInstanceIdentifier",
                str(value["target_db_instance_identifier"]),
            )
        )


def deserialize_query(el: Element) -> FailoverDBClusterMessage:
    out: FailoverDBClusterMessage = {}  # type: ignore[typeddict-item]
    child_db_cluster_identifier = el.find("DBClusterIdentifier")
    if child_db_cluster_identifier is not None:
        out["db_cluster_identifier"] = str(child_db_cluster_identifier.text or "")
    child_target_db_instance_identifier = el.find("TargetDBInstanceIdentifier")
    if child_target_db_instance_identifier is not None:
        out["target_db_instance_identifier"] = str(
            child_target_db_instance_identifier.text or ""
        )
    return out
