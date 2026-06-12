"""Generated from Smithy shape ``com.amazonaws.dax#DeleteClusterResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dax.types.cluster


class DeleteClusterResponse(TypedDict):
    cluster: NotRequired["aws_sdk_dax.types.cluster.Cluster"]
    """<p>A description of the DAX cluster that is being deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteClusterResponse) -> dict:
    out: dict = {}
    if "cluster" in value:
        import aws_sdk_dax.types.cluster

        out["Cluster"] = aws_sdk_dax.types.cluster.serialize_aws_json_1_1(
            value["cluster"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteClusterResponse:
    out: DeleteClusterResponse = {}  # type: ignore[typeddict-item]
    if "Cluster" in data:
        import aws_sdk_dax.types.cluster

        out["cluster"] = aws_sdk_dax.types.cluster.deserialize_aws_json_1_1(
            data["Cluster"]
        )
    return out
