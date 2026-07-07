"""Generated from Smithy shape ``com.amazonaws.memorydb#BatchUpdateClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_memorydb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.cluster_name_list
    import aws_sdk_memorydb.types.service_update_request


class BatchUpdateClusterRequest(TypedDict, closed=True):
    cluster_names: "aws_sdk_memorydb.types.cluster_name_list.ClusterNameList"
    """<p>The cluster names to apply the updates.</p>"""
    service_update: NotRequired[
        "aws_sdk_memorydb.types.service_update_request.ServiceUpdateRequest"
    ]
    """<p>The unique ID of the service update</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchUpdateClusterRequest) -> dict:
    out: dict = {}
    import aws_sdk_memorydb.types.cluster_name_list

    out["ClusterNames"] = (
        aws_sdk_memorydb.types.cluster_name_list.serialize_aws_json_1_1(
            value["cluster_names"]
        )
    )
    if "service_update" in value:
        import aws_sdk_memorydb.types.service_update_request

        out["ServiceUpdate"] = (
            aws_sdk_memorydb.types.service_update_request.serialize_aws_json_1_1(
                value["service_update"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchUpdateClusterRequest:
    out: BatchUpdateClusterRequest = {}  # type: ignore[typeddict-item]
    if "ClusterNames" in data:
        import aws_sdk_memorydb.types.cluster_name_list

        out["cluster_names"] = (
            aws_sdk_memorydb.types.cluster_name_list.deserialize_aws_json_1_1(
                data["ClusterNames"]
            )
        )
    else:
        raise DeserializationError("BatchUpdateClusterRequest.cluster_names required")
    if "ServiceUpdate" in data:
        import aws_sdk_memorydb.types.service_update_request

        out["service_update"] = (
            aws_sdk_memorydb.types.service_update_request.deserialize_aws_json_1_1(
                data["ServiceUpdate"]
            )
        )
    return out
