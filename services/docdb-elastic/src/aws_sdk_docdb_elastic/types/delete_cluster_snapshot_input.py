"""Generated from Smithy shape ``com.amazonaws.docdbelastic#DeleteClusterSnapshotInput``."""

from typing_extensions import TypedDict


class DeleteClusterSnapshotInput(TypedDict, closed=True):
    snapshot_arn: "str"
    """<p>The ARN identifier of the elastic cluster snapshot that is to be deleted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteClusterSnapshotInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteClusterSnapshotInput:
    out: DeleteClusterSnapshotInput = {}  # type: ignore[typeddict-item]
    return out
