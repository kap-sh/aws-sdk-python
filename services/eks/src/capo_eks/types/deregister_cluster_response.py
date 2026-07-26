"""Generated from Smithy shape ``com.amazonaws.eks#DeregisterClusterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_eks.types.cluster


class DeregisterClusterResponse(TypedDict, closed=True):
    cluster: NotRequired["capo_eks.types.cluster.Cluster"]


# --- restJson1 ser/de ---
def serialize_json(value: DeregisterClusterResponse) -> dict:
    out: dict = {}
    if "cluster" in value:
        import capo_eks.types.cluster

        out["cluster"] = capo_eks.types.cluster.serialize_json(value["cluster"])
    return out


def deserialize_json(data: dict) -> DeregisterClusterResponse:
    out: DeregisterClusterResponse = {}  # type: ignore[typeddict-item]
    if "cluster" in data:
        import capo_eks.types.cluster

        out["cluster"] = capo_eks.types.cluster.deserialize_json(data["cluster"])
    return out
