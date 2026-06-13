"""Generated from Smithy shape ``com.amazonaws.neptunegraph#GetGraphSnapshotInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_neptune_graph.types.snapshot_identifier


class GetGraphSnapshotInput(TypedDict):
    snapshot_identifier: (
        "aws_sdk_neptune_graph.types.snapshot_identifier.SnapshotIdentifier"
    )
    """<p>The ID of the snapshot to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGraphSnapshotInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetGraphSnapshotInput:
    out: GetGraphSnapshotInput = {}  # type: ignore[typeddict-item]
    return out
