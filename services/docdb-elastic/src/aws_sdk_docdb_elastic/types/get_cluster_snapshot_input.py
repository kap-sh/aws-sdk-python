"""Generated from Smithy shape ``com.amazonaws.docdbelastic#GetClusterSnapshotInput``."""

from typing_extensions import TypedDict


class GetClusterSnapshotInput(TypedDict, closed=True):
    snapshot_arn: "str"
    """<p>The ARN identifier of the elastic cluster snapshot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetClusterSnapshotInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetClusterSnapshotInput:
    out: GetClusterSnapshotInput = {}  # type: ignore[typeddict-item]
    return out
