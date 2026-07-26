"""Generated from Smithy shape ``com.amazonaws.rds#DeleteDBClusterAutomatedBackupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string


class DeleteDBClusterAutomatedBackupMessage(TypedDict, closed=True):
    db_cluster_resource_id: NotRequired["capo_rds.types.string.String"]
    """<p>The identifier for the source DB cluster, which can't be changed and which is unique to an Amazon Web Services Region.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteDBClusterAutomatedBackupMessage,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "db_cluster_resource_id" in value:
        pairs.append(
            (f"{prefix}.DbClusterResourceId", str(value["db_cluster_resource_id"]))
        )


def deserialize_query(el: Element) -> DeleteDBClusterAutomatedBackupMessage:
    out: DeleteDBClusterAutomatedBackupMessage = {}  # type: ignore[typeddict-item]
    child_db_cluster_resource_id = el.find("DbClusterResourceId")
    if child_db_cluster_resource_id is not None:
        out["db_cluster_resource_id"] = str(child_db_cluster_resource_id.text or "")
    return out
