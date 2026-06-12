"""Generated from Smithy shape ``com.amazonaws.fsx#UpdateSnapshotResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_fsx.types.snapshot


class UpdateSnapshotResponse(TypedDict):
    snapshot: NotRequired["aws_sdk_fsx.types.snapshot.Snapshot"]
    """<p>Returned after a successful <code>UpdateSnapshot</code> operation, describing the snapshot that you updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSnapshotResponse) -> dict:
    out: dict = {}
    if "snapshot" in value:
        import aws_sdk_fsx.types.snapshot

        out["Snapshot"] = aws_sdk_fsx.types.snapshot.serialize_aws_json_1_1(
            value["snapshot"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSnapshotResponse:
    out: UpdateSnapshotResponse = {}  # type: ignore[typeddict-item]
    if "Snapshot" in data:
        import aws_sdk_fsx.types.snapshot

        out["snapshot"] = aws_sdk_fsx.types.snapshot.deserialize_aws_json_1_1(
            data["Snapshot"]
        )
    return out
