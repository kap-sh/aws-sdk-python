"""Generated from Smithy shape ``com.amazonaws.redshift#DeleteSnapshotCopyGrantMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import capo_redshift.types.string


class DeleteSnapshotCopyGrantMessage(TypedDict, closed=True):
    snapshot_copy_grant_name: NotRequired["capo_redshift.types.string.String"]
    """<p>The name of the snapshot copy grant to delete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteSnapshotCopyGrantMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "snapshot_copy_grant_name" in value:
        pairs.append(
            (
                f"{key_prefix}SnapshotCopyGrantName",
                str(value["snapshot_copy_grant_name"]),
            )
        )


def deserialize_query(el: Element) -> DeleteSnapshotCopyGrantMessage:
    out: DeleteSnapshotCopyGrantMessage = {}  # type: ignore[typeddict-item]
    child_snapshot_copy_grant_name = el.find("SnapshotCopyGrantName")
    if child_snapshot_copy_grant_name is not None:
        out["snapshot_copy_grant_name"] = str(child_snapshot_copy_grant_name.text or "")
    return out
