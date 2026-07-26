"""Generated from Smithy shape ``com.amazonaws.rds#DeleteDBSnapshotMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string


class DeleteDBSnapshotMessage(TypedDict, closed=True):
    db_snapshot_identifier: NotRequired["capo_rds.types.string.String"]
    """<p>The DB snapshot identifier.</p> <p>Constraints: Must be the name of an existing DB snapshot in the <code>available</code> state.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteDBSnapshotMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "db_snapshot_identifier" in value:
        pairs.append(
            (f"{prefix}.DBSnapshotIdentifier", str(value["db_snapshot_identifier"]))
        )


def deserialize_query(el: Element) -> DeleteDBSnapshotMessage:
    out: DeleteDBSnapshotMessage = {}  # type: ignore[typeddict-item]
    child_db_snapshot_identifier = el.find("DBSnapshotIdentifier")
    if child_db_snapshot_identifier is not None:
        out["db_snapshot_identifier"] = str(child_db_snapshot_identifier.text or "")
    return out
