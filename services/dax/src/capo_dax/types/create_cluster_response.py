"""Generated from Smithy shape ``com.amazonaws.dax#CreateClusterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dax.types.cluster


class CreateClusterResponse(TypedDict, closed=True):
    cluster: NotRequired["capo_dax.types.cluster.Cluster"]
    """<p>A description of the DAX cluster that you have created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateClusterResponse) -> dict:
    out: dict = {}
    if "cluster" in value:
        import capo_dax.types.cluster

        out["Cluster"] = capo_dax.types.cluster.serialize_aws_json_1_1(value["cluster"])
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateClusterResponse:
    out: CreateClusterResponse = {}  # type: ignore[typeddict-item]
    if "Cluster" in data:
        import capo_dax.types.cluster

        out["cluster"] = capo_dax.types.cluster.deserialize_aws_json_1_1(
            data["Cluster"]
        )
    return out
