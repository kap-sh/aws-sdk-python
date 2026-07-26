"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteClusterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.cluster


class DeleteClusterResponse(TypedDict, closed=True):
    cluster: NotRequired["capo_ecs.types.cluster.Cluster"]
    """<p>The full description of the deleted cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteClusterResponse) -> dict:
    out: dict = {}
    if "cluster" in value:
        import capo_ecs.types.cluster

        out["cluster"] = capo_ecs.types.cluster.serialize_aws_json_1_1(value["cluster"])
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteClusterResponse:
    out: DeleteClusterResponse = {}  # type: ignore[typeddict-item]
    if "cluster" in data:
        import capo_ecs.types.cluster

        out["cluster"] = capo_ecs.types.cluster.deserialize_aws_json_1_1(
            data["cluster"]
        )
    return out
