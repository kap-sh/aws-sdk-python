"""Generated from Smithy shape ``com.amazonaws.elasticache#DeleteSnapshotMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.string


class DeleteSnapshotMessage(TypedDict):
    snapshot_name: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The name of the snapshot to be deleted.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteSnapshotMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "snapshot_name" in value:
        pairs.append((f"{prefix}.SnapshotName", str(value["snapshot_name"])))


def deserialize_query(el: Element) -> DeleteSnapshotMessage:
    out: DeleteSnapshotMessage = {}  # type: ignore[typeddict-item]
    child_snapshot_name = el.find("SnapshotName")
    if child_snapshot_name is not None:
        out["snapshot_name"] = str(child_snapshot_name.text or "")
    return out
