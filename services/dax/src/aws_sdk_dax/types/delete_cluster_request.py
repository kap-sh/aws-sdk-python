"""Generated from Smithy shape ``com.amazonaws.dax#DeleteClusterRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_dax.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dax.types.string


class DeleteClusterRequest(TypedDict):
    cluster_name: "aws_sdk_dax.types.string.String"
    """<p>The name of the cluster to be deleted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteClusterRequest) -> dict:
    out: dict = {}
    out["ClusterName"] = value["cluster_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteClusterRequest:
    out: DeleteClusterRequest = {}  # type: ignore[typeddict-item]
    if "ClusterName" in data:
        out["cluster_name"] = data["ClusterName"]
    else:
        raise DeserializationError("DeleteClusterRequest.cluster_name required")
    return out
