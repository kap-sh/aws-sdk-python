"""Generated from Smithy shape ``com.amazonaws.docdbelastic#CopyClusterSnapshotOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_docdb_elastic.errors import DeserializationError

if TYPE_CHECKING:
    import capo_docdb_elastic.types.cluster_snapshot


class CopyClusterSnapshotOutput(TypedDict, closed=True):
    snapshot: "capo_docdb_elastic.types.cluster_snapshot.ClusterSnapshot"


# --- restJson1 ser/de ---
def serialize_json(value: CopyClusterSnapshotOutput) -> dict:
    out: dict = {}
    import capo_docdb_elastic.types.cluster_snapshot

    out["snapshot"] = capo_docdb_elastic.types.cluster_snapshot.serialize_json(
        value["snapshot"]
    )
    return out


def deserialize_json(data: dict) -> CopyClusterSnapshotOutput:
    out: CopyClusterSnapshotOutput = {}  # type: ignore[typeddict-item]
    if "snapshot" in data:
        import capo_docdb_elastic.types.cluster_snapshot

        out["snapshot"] = capo_docdb_elastic.types.cluster_snapshot.deserialize_json(
            data["snapshot"]
        )
    else:
        raise DeserializationError("CopyClusterSnapshotOutput.snapshot required")
    return out
