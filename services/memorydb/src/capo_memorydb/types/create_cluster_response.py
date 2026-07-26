"""Generated from Smithy shape ``com.amazonaws.memorydb#CreateClusterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.cluster


class CreateClusterResponse(TypedDict, closed=True):
    cluster: NotRequired["capo_memorydb.types.cluster.Cluster"]
    """<p>The newly-created cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateClusterResponse) -> dict:
    out: dict = {}
    if "cluster" in value:
        import capo_memorydb.types.cluster

        out["Cluster"] = capo_memorydb.types.cluster.serialize_aws_json_1_1(
            value["cluster"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateClusterResponse:
    out: CreateClusterResponse = {}  # type: ignore[typeddict-item]
    if "Cluster" in data:
        import capo_memorydb.types.cluster

        out["cluster"] = capo_memorydb.types.cluster.deserialize_aws_json_1_1(
            data["Cluster"]
        )
    return out
