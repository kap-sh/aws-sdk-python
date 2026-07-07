"""Generated from Smithy shape ``com.amazonaws.memorydb#BatchUpdateClusterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.cluster_list
    import aws_sdk_memorydb.types.unprocessed_cluster_list


class BatchUpdateClusterResponse(TypedDict, closed=True):
    processed_clusters: NotRequired["aws_sdk_memorydb.types.cluster_list.ClusterList"]
    """<p>The list of clusters that have been updated.</p>"""
    unprocessed_clusters: NotRequired[
        "aws_sdk_memorydb.types.unprocessed_cluster_list.UnprocessedClusterList"
    ]
    """<p>The list of clusters where updates have not been applied.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchUpdateClusterResponse) -> dict:
    out: dict = {}
    if "processed_clusters" in value:
        import aws_sdk_memorydb.types.cluster_list

        out["ProcessedClusters"] = (
            aws_sdk_memorydb.types.cluster_list.serialize_aws_json_1_1(
                value["processed_clusters"]
            )
        )
    if "unprocessed_clusters" in value:
        import aws_sdk_memorydb.types.unprocessed_cluster_list

        out["UnprocessedClusters"] = (
            aws_sdk_memorydb.types.unprocessed_cluster_list.serialize_aws_json_1_1(
                value["unprocessed_clusters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchUpdateClusterResponse:
    out: BatchUpdateClusterResponse = {}  # type: ignore[typeddict-item]
    if "ProcessedClusters" in data:
        import aws_sdk_memorydb.types.cluster_list

        out["processed_clusters"] = (
            aws_sdk_memorydb.types.cluster_list.deserialize_aws_json_1_1(
                data["ProcessedClusters"]
            )
        )
    if "UnprocessedClusters" in data:
        import aws_sdk_memorydb.types.unprocessed_cluster_list

        out["unprocessed_clusters"] = (
            aws_sdk_memorydb.types.unprocessed_cluster_list.deserialize_aws_json_1_1(
                data["UnprocessedClusters"]
            )
        )
    return out
