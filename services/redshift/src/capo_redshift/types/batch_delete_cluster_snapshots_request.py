"""Generated from Smithy shape ``com.amazonaws.redshift#BatchDeleteClusterSnapshotsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.delete_cluster_snapshot_message_list


class BatchDeleteClusterSnapshotsRequest(TypedDict, closed=True):
    identifiers: NotRequired[
        "capo_redshift.types.delete_cluster_snapshot_message_list.DeleteClusterSnapshotMessageList"
    ]
    """<p>A list of identifiers for the snapshots that you want to delete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: BatchDeleteClusterSnapshotsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "identifiers" in value:
        import capo_redshift.types.delete_cluster_snapshot_message_list

        capo_redshift.types.delete_cluster_snapshot_message_list.serialize_query(
            value["identifiers"], pairs, f"{prefix}.Identifiers"
        )


def deserialize_query(el: Element) -> BatchDeleteClusterSnapshotsRequest:
    out: BatchDeleteClusterSnapshotsRequest = {}  # type: ignore[typeddict-item]
    child_identifiers = el.find("Identifiers")
    if child_identifiers is not None:
        import capo_redshift.types.delete_cluster_snapshot_message_list

        out["identifiers"] = (
            capo_redshift.types.delete_cluster_snapshot_message_list.deserialize_query(
                child_identifiers
            )
        )
    return out
