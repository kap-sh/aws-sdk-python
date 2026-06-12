"""Generated from Smithy shape ``com.amazonaws.memorydb#ListAllowedMultiRegionClusterUpdatesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_memorydb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.string


class ListAllowedMultiRegionClusterUpdatesRequest(TypedDict):
    multi_region_cluster_name: "aws_sdk_memorydb.types.string.String"
    """<p>The name of the multi-Region cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAllowedMultiRegionClusterUpdatesRequest) -> dict:
    out: dict = {}
    out["MultiRegionClusterName"] = value["multi_region_cluster_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAllowedMultiRegionClusterUpdatesRequest:
    out: ListAllowedMultiRegionClusterUpdatesRequest = {}  # type: ignore[typeddict-item]
    if "MultiRegionClusterName" in data:
        out["multi_region_cluster_name"] = data["MultiRegionClusterName"]
    else:
        raise DeserializationError(
            "ListAllowedMultiRegionClusterUpdatesRequest.multi_region_cluster_name required"
        )
    return out
