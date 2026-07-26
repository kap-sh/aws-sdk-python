"""Generated from Smithy shape ``com.amazonaws.kafka#ListClusterOperationsV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__list_of_cluster_operation_v2_summary
    import capo_kafka.types.__string


class ListClusterOperationsV2Response(TypedDict, closed=True):
    cluster_operation_info_list: NotRequired[
        "capo_kafka.types.__list_of_cluster_operation_v2_summary.__listOfClusterOperationV2Summary"
    ]
    """<p>An array of cluster operation information objects.</p>"""
    next_token: NotRequired["capo_kafka.types.__string.__string"]
    """<p>If the response of ListClusterOperationsV2 is truncated, it returns a NextToken in the response. This NextToken should be sent in the subsequent request to ListClusterOperationsV2.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListClusterOperationsV2Response) -> dict:
    out: dict = {}
    if "cluster_operation_info_list" in value:
        import capo_kafka.types.__list_of_cluster_operation_v2_summary

        out["clusterOperationInfoList"] = (
            capo_kafka.types.__list_of_cluster_operation_v2_summary.serialize_json(
                value["cluster_operation_info_list"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListClusterOperationsV2Response:
    out: ListClusterOperationsV2Response = {}  # type: ignore[typeddict-item]
    if "clusterOperationInfoList" in data:
        import capo_kafka.types.__list_of_cluster_operation_v2_summary

        out["cluster_operation_info_list"] = (
            capo_kafka.types.__list_of_cluster_operation_v2_summary.deserialize_json(
                data["clusterOperationInfoList"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
