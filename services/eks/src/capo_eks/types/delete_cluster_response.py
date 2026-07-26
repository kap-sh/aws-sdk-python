"""Generated from Smithy shape ``com.amazonaws.eks#DeleteClusterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.cluster


class DeleteClusterResponse(TypedDict, closed=True):
    cluster: NotRequired["capo_eks.types.cluster.Cluster"]
    """<p>The full description of the cluster to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteClusterResponse) -> dict:
    out: dict = {}
    if "cluster" in value:
        import capo_eks.types.cluster

        out["cluster"] = capo_eks.types.cluster.serialize_json(value["cluster"])
    return out


def deserialize_json(data: dict) -> DeleteClusterResponse:
    out: DeleteClusterResponse = {}  # type: ignore[typeddict-item]
    if "cluster" in data:
        import capo_eks.types.cluster

        out["cluster"] = capo_eks.types.cluster.deserialize_json(data["cluster"])
    return out
