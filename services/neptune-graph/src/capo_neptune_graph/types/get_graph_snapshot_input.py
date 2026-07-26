"""Generated from Smithy shape ``com.amazonaws.neptunegraph#GetGraphSnapshotInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_neptune_graph.types.snapshot_identifier


class GetGraphSnapshotInput(TypedDict, closed=True):
    snapshot_identifier: (
        "capo_neptune_graph.types.snapshot_identifier.SnapshotIdentifier"
    )
    """<p>The ID of the snapshot to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGraphSnapshotInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetGraphSnapshotInput:
    out: GetGraphSnapshotInput = {}  # type: ignore[typeddict-item]
    return out
