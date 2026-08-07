"""Generated from Smithy shape ``com.amazonaws.neptune#PromoteReadReplicaDBClusterMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import capo_neptune.types.string


class PromoteReadReplicaDBClusterMessage(TypedDict, closed=True):
    db_cluster_identifier: NotRequired["capo_neptune.types.string.String"]
    """<p>Not supported.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PromoteReadReplicaDBClusterMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_cluster_identifier" in value:
        pairs.append(
            (f"{key_prefix}DBClusterIdentifier", str(value["db_cluster_identifier"]))
        )


def deserialize_query(el: Element) -> PromoteReadReplicaDBClusterMessage:
    out: PromoteReadReplicaDBClusterMessage = {}  # type: ignore[typeddict-item]
    child_db_cluster_identifier = el.find("DBClusterIdentifier")
    if child_db_cluster_identifier is not None:
        out["db_cluster_identifier"] = str(child_db_cluster_identifier.text or "")
    return out
