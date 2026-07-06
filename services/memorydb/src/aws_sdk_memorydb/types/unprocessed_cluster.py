"""Generated from Smithy shape ``com.amazonaws.memorydb#UnprocessedCluster``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.string


class UnprocessedCluster(TypedDict, closed=True):
    cluster_name: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The name of the cluster</p>"""
    error_type: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The error type associated with the update failure</p>"""
    error_message: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The error message associated with the update failure</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnprocessedCluster) -> dict:
    out: dict = {}
    if "cluster_name" in value:
        out["ClusterName"] = value["cluster_name"]
    if "error_type" in value:
        out["ErrorType"] = value["error_type"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UnprocessedCluster:
    out: UnprocessedCluster = {}  # type: ignore[typeddict-item]
    if "ClusterName" in data:
        out["cluster_name"] = data["ClusterName"]
    if "ErrorType" in data:
        out["error_type"] = data["ErrorType"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
