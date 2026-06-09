"""Generated from Smithy shape ``com.amazonaws.eks#RegisterClusterResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_eks.types.cluster


class RegisterClusterResponse(TypedDict):
    cluster: NotRequired["aws_sdk_eks.types.cluster.Cluster"]


# --- restJson1 ser/de ---
def serialize_json(value: RegisterClusterResponse) -> dict:
    out: dict = {}
    if "cluster" in value:
        import aws_sdk_eks.types.cluster

        out["cluster"] = aws_sdk_eks.types.cluster.serialize_json(value["cluster"])
    return out


def deserialize_json(data: dict) -> RegisterClusterResponse:
    out: RegisterClusterResponse = {}  # type: ignore[typeddict-item]
    if "cluster" in data:
        import aws_sdk_eks.types.cluster

        out["cluster"] = aws_sdk_eks.types.cluster.deserialize_json(data["cluster"])
    return out
