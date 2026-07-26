"""Generated from Smithy shape ``com.amazonaws.neptunegraph#DeleteGraphSnapshotInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_neptune_graph.types.snapshot_identifier


class DeleteGraphSnapshotInput(TypedDict, closed=True):
    snapshot_identifier: (
        "capo_neptune_graph.types.snapshot_identifier.SnapshotIdentifier"
    )
    """<p>ID of the graph snapshot to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGraphSnapshotInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteGraphSnapshotInput:
    out: DeleteGraphSnapshotInput = {}  # type: ignore[typeddict-item]
    return out
