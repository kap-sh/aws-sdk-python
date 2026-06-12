"""Generated from Smithy shape ``com.amazonaws.kafka#ListClustersResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__list_of_cluster_info
    import aws_sdk_kafka.types.__string


class ListClustersResponse(TypedDict):
    cluster_info_list: NotRequired[
        "aws_sdk_kafka.types.__list_of_cluster_info.__listOfClusterInfo"
    ]
    """<p>Information on each of the MSK clusters in the response.</p>"""
    next_token: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The paginated results marker. When the result of a ListClusters operation is truncated, the call returns NextToken in the response. To get another batch of clusters, provide this token in your next request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListClustersResponse) -> dict:
    out: dict = {}
    if "cluster_info_list" in value:
        import aws_sdk_kafka.types.__list_of_cluster_info

        out["clusterInfoList"] = (
            aws_sdk_kafka.types.__list_of_cluster_info.serialize_json(
                value["cluster_info_list"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListClustersResponse:
    out: ListClustersResponse = {}  # type: ignore[typeddict-item]
    if "clusterInfoList" in data:
        import aws_sdk_kafka.types.__list_of_cluster_info

        out["cluster_info_list"] = (
            aws_sdk_kafka.types.__list_of_cluster_info.deserialize_json(
                data["clusterInfoList"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
