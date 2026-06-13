"""Generated from Smithy shape ``com.amazonaws.neptunegraph#DeleteGraphSnapshotInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.snapshot_identifier


class DeleteGraphSnapshotInput(TypedDict):
    snapshot_identifier: (
        "aws_sdk_neptune_graph.types.snapshot_identifier.SnapshotIdentifier"
    )
    """<p>ID of the graph snapshot to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteGraphSnapshotInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteGraphSnapshotInput:
    out: DeleteGraphSnapshotInput = {}  # type: ignore[typeddict-item]
    return out
