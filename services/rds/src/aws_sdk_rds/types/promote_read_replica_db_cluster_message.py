"""Generated from Smithy shape ``com.amazonaws.rds#PromoteReadReplicaDBClusterMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.string


class PromoteReadReplicaDBClusterMessage(TypedDict, closed=True):
    db_cluster_identifier: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The identifier of the DB cluster read replica to promote. This parameter isn't case-sensitive.</p> <p>Constraints:</p> <ul> <li> <p>Must match the identifier of an existing DB cluster read replica.</p> </li> </ul> <p>Example: <code>my-cluster-replica1</code> </p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PromoteReadReplicaDBClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{prefix}.DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )


def deserialize_query(el: Element) -> PromoteReadReplicaDBClusterMessage:
    out: PromoteReadReplicaDBClusterMessage = {}  # type: ignore[typeddict-item]
    child_db_cluster_identifier = el.find("DBClusterIdentifier")
    if child_db_cluster_identifier is not None:
        out["db_cluster_identifier"] = str(child_db_cluster_identifier.text or "")
    return out
