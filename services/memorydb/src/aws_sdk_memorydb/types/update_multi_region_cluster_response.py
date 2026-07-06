"""Generated from Smithy shape ``com.amazonaws.memorydb#UpdateMultiRegionClusterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.multi_region_cluster


class UpdateMultiRegionClusterResponse(TypedDict, closed=True):
    multi_region_cluster: NotRequired[
        "aws_sdk_memorydb.types.multi_region_cluster.MultiRegionCluster"
    ]
    """<p>The status of updating the multi-Region cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateMultiRegionClusterResponse) -> dict:
    out: dict = {}
    if "multi_region_cluster" in value:
        import aws_sdk_memorydb.types.multi_region_cluster

        out["MultiRegionCluster"] = (
            aws_sdk_memorydb.types.multi_region_cluster.serialize_aws_json_1_1(
                value["multi_region_cluster"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateMultiRegionClusterResponse:
    out: UpdateMultiRegionClusterResponse = {}  # type: ignore[typeddict-item]
    if "MultiRegionCluster" in data:
        import aws_sdk_memorydb.types.multi_region_cluster

        out["multi_region_cluster"] = (
            aws_sdk_memorydb.types.multi_region_cluster.deserialize_aws_json_1_1(
                data["MultiRegionCluster"]
            )
        )
    return out
