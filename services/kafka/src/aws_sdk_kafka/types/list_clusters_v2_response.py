"""Generated from Smithy shape ``com.amazonaws.kafka#ListClustersV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__list_of_cluster
    import aws_sdk_kafka.types.__string


class ListClustersV2Response(TypedDict, closed=True):
    cluster_info_list: NotRequired[
        "aws_sdk_kafka.types.__list_of_cluster.__listOfCluster"
    ]
    """<p>Information on each of the MSK clusters in the response.</p>"""
    next_token: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The paginated results marker. When the result of a ListClusters operation is truncated, the call returns NextToken in the response. To get another batch of clusters, provide this token in your next request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListClustersV2Response) -> dict:
    out: dict = {}
    if "cluster_info_list" in value:
        import aws_sdk_kafka.types.__list_of_cluster

        out["clusterInfoList"] = aws_sdk_kafka.types.__list_of_cluster.serialize_json(
            value["cluster_info_list"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListClustersV2Response:
    out: ListClustersV2Response = {}  # type: ignore[typeddict-item]
    if "clusterInfoList" in data:
        import aws_sdk_kafka.types.__list_of_cluster

        out["cluster_info_list"] = (
            aws_sdk_kafka.types.__list_of_cluster.deserialize_json(
                data["clusterInfoList"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
