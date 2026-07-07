"""Generated from Smithy shape ``com.amazonaws.docdbelastic#RestoreClusterFromSnapshotOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_docdb_elastic.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_docdb_elastic.types.cluster


class RestoreClusterFromSnapshotOutput(TypedDict, closed=True):
    cluster: "aws_sdk_docdb_elastic.types.cluster.Cluster"
    """<p>Returns information about a the restored elastic cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RestoreClusterFromSnapshotOutput) -> dict:
    out: dict = {}
    import aws_sdk_docdb_elastic.types.cluster

    out["cluster"] = aws_sdk_docdb_elastic.types.cluster.serialize_json(
        value["cluster"]
    )
    return out


def deserialize_json(data: dict) -> RestoreClusterFromSnapshotOutput:
    out: RestoreClusterFromSnapshotOutput = {}  # type: ignore[typeddict-item]
    if "cluster" in data:
        import aws_sdk_docdb_elastic.types.cluster

        out["cluster"] = aws_sdk_docdb_elastic.types.cluster.deserialize_json(
            data["cluster"]
        )
    else:
        raise DeserializationError("RestoreClusterFromSnapshotOutput.cluster required")
    return out
