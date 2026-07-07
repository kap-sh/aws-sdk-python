"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#CreateClusterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cloudhsm_v2.types.cluster


class CreateClusterResponse(TypedDict, closed=True):
    cluster: NotRequired["aws_sdk_cloudhsm_v2.types.cluster.Cluster"]
    """<p>Information about the cluster that was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateClusterResponse) -> dict:
    out: dict = {}
    if "cluster" in value:
        import aws_sdk_cloudhsm_v2.types.cluster

        out["Cluster"] = aws_sdk_cloudhsm_v2.types.cluster.serialize_aws_json_1_1(
            value["cluster"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateClusterResponse:
    out: CreateClusterResponse = {}  # type: ignore[typeddict-item]
    if "Cluster" in data:
        import aws_sdk_cloudhsm_v2.types.cluster

        out["cluster"] = aws_sdk_cloudhsm_v2.types.cluster.deserialize_aws_json_1_1(
            data["Cluster"]
        )
    return out
