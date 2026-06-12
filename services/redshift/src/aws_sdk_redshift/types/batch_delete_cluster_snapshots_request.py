"""Generated from Smithy shape ``com.amazonaws.redshift#BatchDeleteClusterSnapshotsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.delete_cluster_snapshot_message_list


class BatchDeleteClusterSnapshotsRequest(TypedDict):
    identifiers: NotRequired[
        "aws_sdk_redshift.types.delete_cluster_snapshot_message_list.DeleteClusterSnapshotMessageList"
    ]
    """<p>A list of identifiers for the snapshots that you want to delete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: BatchDeleteClusterSnapshotsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "identifiers" in value:
        import aws_sdk_redshift.types.delete_cluster_snapshot_message_list

        aws_sdk_redshift.types.delete_cluster_snapshot_message_list.serialize_query(
            value["identifiers"], pairs, f"{prefix}.Identifiers"
        )


def deserialize_query(el: Element) -> BatchDeleteClusterSnapshotsRequest:
    out: BatchDeleteClusterSnapshotsRequest = {}  # type: ignore[typeddict-item]
    child_identifiers = el.find("Identifiers")
    if child_identifiers is not None:
        import aws_sdk_redshift.types.delete_cluster_snapshot_message_list

        out["identifiers"] = (
            aws_sdk_redshift.types.delete_cluster_snapshot_message_list.deserialize_query(
                child_identifiers
            )
        )
    return out
