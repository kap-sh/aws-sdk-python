"""Generated from Smithy shape ``com.amazonaws.pcs#CreateClusterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pcs.types.cluster


class CreateClusterResponse(TypedDict, closed=True):
    cluster: NotRequired["capo_pcs.types.cluster.Cluster"]
    """<p>The cluster resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateClusterResponse) -> dict:
    out: dict = {}
    if "cluster" in value:
        import capo_pcs.types.cluster

        out["cluster"] = capo_pcs.types.cluster.serialize_aws_json_1_0(value["cluster"])
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateClusterResponse:
    out: CreateClusterResponse = {}  # type: ignore[typeddict-item]
    if "cluster" in data:
        import capo_pcs.types.cluster

        out["cluster"] = capo_pcs.types.cluster.deserialize_aws_json_1_0(
            data["cluster"]
        )
    return out
