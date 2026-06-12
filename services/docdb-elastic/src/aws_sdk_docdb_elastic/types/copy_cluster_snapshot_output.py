"""Generated from Smithy shape ``com.amazonaws.docdbelastic#CopyClusterSnapshotOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_docdb_elastic.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_docdb_elastic.types.cluster_snapshot


class CopyClusterSnapshotOutput(TypedDict):
    snapshot: "aws_sdk_docdb_elastic.types.cluster_snapshot.ClusterSnapshot"


# --- restJson1 ser/de ---
def serialize_json(value: CopyClusterSnapshotOutput) -> dict:
    out: dict = {}
    import aws_sdk_docdb_elastic.types.cluster_snapshot

    out["snapshot"] = aws_sdk_docdb_elastic.types.cluster_snapshot.serialize_json(
        value["snapshot"]
    )
    return out


def deserialize_json(data: dict) -> CopyClusterSnapshotOutput:
    out: CopyClusterSnapshotOutput = {}  # type: ignore[typeddict-item]
    if "snapshot" in data:
        import aws_sdk_docdb_elastic.types.cluster_snapshot

        out["snapshot"] = aws_sdk_docdb_elastic.types.cluster_snapshot.deserialize_json(
            data["snapshot"]
        )
    else:
        raise DeserializationError("CopyClusterSnapshotOutput.snapshot required")
    return out
