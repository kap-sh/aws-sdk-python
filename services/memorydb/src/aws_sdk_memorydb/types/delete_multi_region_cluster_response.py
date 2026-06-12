"""Generated from Smithy shape ``com.amazonaws.memorydb#DeleteMultiRegionClusterResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.multi_region_cluster


class DeleteMultiRegionClusterResponse(TypedDict):
    multi_region_cluster: NotRequired[
        "aws_sdk_memorydb.types.multi_region_cluster.MultiRegionCluster"
    ]
    """<p>Details about the deleted multi-Region cluster.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteMultiRegionClusterResponse) -> dict:
    out: dict = {}
    if "multi_region_cluster" in value:
        import aws_sdk_memorydb.types.multi_region_cluster

        out["MultiRegionCluster"] = (
            aws_sdk_memorydb.types.multi_region_cluster.serialize_aws_json_1_1(
                value["multi_region_cluster"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteMultiRegionClusterResponse:
    out: DeleteMultiRegionClusterResponse = {}  # type: ignore[typeddict-item]
    if "MultiRegionCluster" in data:
        import aws_sdk_memorydb.types.multi_region_cluster

        out["multi_region_cluster"] = (
            aws_sdk_memorydb.types.multi_region_cluster.deserialize_aws_json_1_1(
                data["MultiRegionCluster"]
            )
        )
    return out
