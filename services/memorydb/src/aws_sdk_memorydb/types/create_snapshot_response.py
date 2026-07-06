"""Generated from Smithy shape ``com.amazonaws.memorydb#CreateSnapshotResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.snapshot


class CreateSnapshotResponse(TypedDict, closed=True):
    snapshot: NotRequired["aws_sdk_memorydb.types.snapshot.Snapshot"]
    """<p>The newly-created snapshot.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateSnapshotResponse) -> dict:
    out: dict = {}
    if "snapshot" in value:
        import aws_sdk_memorydb.types.snapshot

        out["Snapshot"] = aws_sdk_memorydb.types.snapshot.serialize_aws_json_1_1(
            value["snapshot"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateSnapshotResponse:
    out: CreateSnapshotResponse = {}  # type: ignore[typeddict-item]
    if "Snapshot" in data:
        import aws_sdk_memorydb.types.snapshot

        out["snapshot"] = aws_sdk_memorydb.types.snapshot.deserialize_aws_json_1_1(
            data["Snapshot"]
        )
    return out
