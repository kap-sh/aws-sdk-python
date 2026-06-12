"""Generated from Smithy shape ``com.amazonaws.docdbelastic#GetClusterSnapshotOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_docdb_elastic.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_docdb_elastic.types.cluster_snapshot


class GetClusterSnapshotOutput(TypedDict):
    snapshot: "aws_sdk_docdb_elastic.types.cluster_snapshot.ClusterSnapshot"
    """<p>Returns information about a specific elastic cluster snapshot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetClusterSnapshotOutput) -> dict:
    out: dict = {}
    import aws_sdk_docdb_elastic.types.cluster_snapshot

    out["snapshot"] = aws_sdk_docdb_elastic.types.cluster_snapshot.serialize_json(
        value["snapshot"]
    )
    return out


def deserialize_json(data: dict) -> GetClusterSnapshotOutput:
    out: GetClusterSnapshotOutput = {}  # type: ignore[typeddict-item]
    if "snapshot" in data:
        import aws_sdk_docdb_elastic.types.cluster_snapshot

        out["snapshot"] = aws_sdk_docdb_elastic.types.cluster_snapshot.deserialize_json(
            data["snapshot"]
        )
    else:
        raise DeserializationError("GetClusterSnapshotOutput.snapshot required")
    return out
