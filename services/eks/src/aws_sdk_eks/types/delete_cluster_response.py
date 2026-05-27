"""Generated from Smithy shape ``com.amazonaws.eks#DeleteClusterResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.cluster


class DeleteClusterResponse(TypedDict):
    cluster: NotRequired["aws_sdk_eks.types.cluster.Cluster"]
    """<p>The full description of the cluster to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteClusterResponse) -> dict:
    out: dict = {}
    if "cluster" in value:
        import aws_sdk_eks.types.cluster

        out["cluster"] = aws_sdk_eks.types.cluster.serialize_json(value["cluster"])
    return out


def deserialize_json(data: dict) -> DeleteClusterResponse:
    out: DeleteClusterResponse = {}  # type: ignore[typeddict-item]
    if "cluster" in data:
        import aws_sdk_eks.types.cluster

        out["cluster"] = aws_sdk_eks.types.cluster.deserialize_json(data["cluster"])
    return out
