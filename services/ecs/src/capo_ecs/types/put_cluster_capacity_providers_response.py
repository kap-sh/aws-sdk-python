"""Generated from Smithy shape ``com.amazonaws.ecs#PutClusterCapacityProvidersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.cluster


class PutClusterCapacityProvidersResponse(TypedDict, closed=True):
    cluster: NotRequired["capo_ecs.types.cluster.Cluster"]
    """<p>Details about the cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutClusterCapacityProvidersResponse) -> dict:
    out: dict = {}
    if "cluster" in value:
        import capo_ecs.types.cluster

        out["cluster"] = capo_ecs.types.cluster.serialize_aws_json_1_1(value["cluster"])
    return out


def deserialize_aws_json_1_1(data: dict) -> PutClusterCapacityProvidersResponse:
    out: PutClusterCapacityProvidersResponse = {}  # type: ignore[typeddict-item]
    if data.get("cluster") is not None:
        import capo_ecs.types.cluster

        out["cluster"] = capo_ecs.types.cluster.deserialize_aws_json_1_1(
            data["cluster"]
        )
    return out
