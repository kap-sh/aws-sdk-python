"""Generated from Smithy shape ``com.amazonaws.snowball#CancelClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_snowball.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_snowball.types.cluster_id


class CancelClusterRequest(TypedDict, closed=True):
    cluster_id: "aws_sdk_snowball.types.cluster_id.ClusterId"
    """<p>The 39-character ID for the cluster that you want to cancel, for example <code>CID123e4567-e89b-12d3-a456-426655440000</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CancelClusterRequest) -> dict:
    out: dict = {}
    out["ClusterId"] = value["cluster_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CancelClusterRequest:
    out: CancelClusterRequest = {}  # type: ignore[typeddict-item]
    if "ClusterId" in data:
        out["cluster_id"] = data["ClusterId"]
    else:
        raise DeserializationError("CancelClusterRequest.cluster_id required")
    return out
