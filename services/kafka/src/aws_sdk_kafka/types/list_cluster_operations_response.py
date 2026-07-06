"""Generated from Smithy shape ``com.amazonaws.kafka#ListClusterOperationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__list_of_cluster_operation_info
    import aws_sdk_kafka.types.__string


class ListClusterOperationsResponse(TypedDict, closed=True):
    cluster_operation_info_list: NotRequired[
        "aws_sdk_kafka.types.__list_of_cluster_operation_info.__listOfClusterOperationInfo"
    ]
    """<p>An array of cluster operation information objects.</p>"""
    next_token: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>If the response of ListClusterOperations is truncated, it returns a NextToken in the response. This Nexttoken should be sent in the subsequent request to ListClusterOperations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListClusterOperationsResponse) -> dict:
    out: dict = {}
    if "cluster_operation_info_list" in value:
        import aws_sdk_kafka.types.__list_of_cluster_operation_info

        out["clusterOperationInfoList"] = (
            aws_sdk_kafka.types.__list_of_cluster_operation_info.serialize_json(
                value["cluster_operation_info_list"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListClusterOperationsResponse:
    out: ListClusterOperationsResponse = {}  # type: ignore[typeddict-item]
    if "clusterOperationInfoList" in data:
        import aws_sdk_kafka.types.__list_of_cluster_operation_info

        out["cluster_operation_info_list"] = (
            aws_sdk_kafka.types.__list_of_cluster_operation_info.deserialize_json(
                data["clusterOperationInfoList"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
