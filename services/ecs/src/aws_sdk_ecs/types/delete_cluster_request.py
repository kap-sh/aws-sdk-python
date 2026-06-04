"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteClusterRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class DeleteClusterRequest(TypedDict):
    cluster: "aws_sdk_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteClusterRequest) -> dict:
    out: dict = {}
    out["cluster"] = value["cluster"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteClusterRequest:
    out: DeleteClusterRequest = {}  # type: ignore[typeddict-item]
    if "cluster" in data:
        out["cluster"] = data["cluster"]
    else:
        raise DeserializationError("DeleteClusterRequest.cluster required")
    return out
