"""Generated from Smithy shape ``com.amazonaws.docdbelastic#DeleteClusterOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_docdb_elastic.errors import DeserializationError

if TYPE_CHECKING:
    import capo_docdb_elastic.types.cluster


class DeleteClusterOutput(TypedDict, closed=True):
    cluster: "capo_docdb_elastic.types.cluster.Cluster"
    """<p>Returns information about the newly deleted elastic cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteClusterOutput) -> dict:
    out: dict = {}
    import capo_docdb_elastic.types.cluster

    out["cluster"] = capo_docdb_elastic.types.cluster.serialize_json(value["cluster"])
    return out


def deserialize_json(data: dict) -> DeleteClusterOutput:
    out: DeleteClusterOutput = {}  # type: ignore[typeddict-item]
    if "cluster" in data:
        import capo_docdb_elastic.types.cluster

        out["cluster"] = capo_docdb_elastic.types.cluster.deserialize_json(
            data["cluster"]
        )
    else:
        raise DeserializationError("DeleteClusterOutput.cluster required")
    return out
