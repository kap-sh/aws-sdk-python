"""Generated from Smithy shape ``com.amazonaws.memorydb#CopySnapshotResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.snapshot


class CopySnapshotResponse(TypedDict):
    snapshot: NotRequired["aws_sdk_memorydb.types.snapshot.Snapshot"]
    """<p>Represents a copy of an entire cluster as of the time when the snapshot was taken.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CopySnapshotResponse) -> dict:
    out: dict = {}
    if "snapshot" in value:
        import aws_sdk_memorydb.types.snapshot

        out["Snapshot"] = aws_sdk_memorydb.types.snapshot.serialize_aws_json_1_1(
            value["snapshot"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CopySnapshotResponse:
    out: CopySnapshotResponse = {}  # type: ignore[typeddict-item]
    if "Snapshot" in data:
        import aws_sdk_memorydb.types.snapshot

        out["snapshot"] = aws_sdk_memorydb.types.snapshot.deserialize_aws_json_1_1(
            data["Snapshot"]
        )
    return out
