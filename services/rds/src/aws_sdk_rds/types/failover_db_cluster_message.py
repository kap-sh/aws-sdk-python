"""Generated from Smithy shape ``com.amazonaws.rds#FailoverDBClusterMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.string


class FailoverDBClusterMessage(TypedDict, closed=True):
    db_cluster_identifier: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The identifier of the DB cluster to force a failover for. This parameter isn't case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing DB cluster.</p> </li> </ul>"""
    target_db_instance_identifier: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The name of the DB instance to promote to the primary DB instance.</p> <p>Specify the DB instance identifier for an Aurora Replica or a Multi-AZ readable standby in the DB cluster, for example <code>mydbcluster-replica1</code>.</p> <p>This setting isn't supported for RDS for MySQL Multi-AZ DB clusters.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: FailoverDBClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{prefix}.DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )
    if "target_db_instance_identifier" in value:
        pairs.append(
            (
                f"{prefix}.TargetDBInstanceIdentifier",
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
