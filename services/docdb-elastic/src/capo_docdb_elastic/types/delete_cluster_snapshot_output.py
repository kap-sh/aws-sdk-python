"""Generated from Smithy shape ``com.amazonaws.docdbelastic#DeleteClusterSnapshotOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_docdb_elastic.errors import DeserializationError

if TYPE_CHECKING:
    import capo_docdb_elastic.types.cluster_snapshot


class DeleteClusterSnapshotOutput(TypedDict, closed=True):
    snapshot: "capo_docdb_elastic.types.cluster_snapshot.ClusterSnapshot"
    """<p>Returns information about the newly deleted elastic cluster snapshot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteClusterSnapshotOutput) -> dict:
    out: dict = {}
    import capo_docdb_elastic.types.cluster_snapshot

    out["snapshot"] = capo_docdb_elastic.types.cluster_snapshot.serialize_json(
        value["snapshot"]
    )
    return out


def deserialize_json(data: dict) -> DeleteClusterSnapshotOutput:
    out: DeleteClusterSnapshotOutput = {}  # type: ignore[typeddict-item]
    if "snapshot" in data:
        import capo_docdb_elastic.types.cluster_snapshot

        out["snapshot"] = capo_docdb_elastic.types.cluster_snapshot.deserialize_json(
            data["snapshot"]
        )
    else:
        raise DeserializationError("DeleteClusterSnapshotOutput.snapshot required")
    return out
