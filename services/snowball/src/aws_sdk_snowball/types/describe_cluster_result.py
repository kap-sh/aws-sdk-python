"""Generated from Smithy shape ``com.amazonaws.snowball#DescribeClusterResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_snowball.types.cluster_metadata


class DescribeClusterResult(TypedDict, closed=True):
    cluster_metadata: NotRequired[
        "aws_sdk_snowball.types.cluster_metadata.ClusterMetadata"
    ]
    """<p>Information about a specific cluster, including shipping information, cluster status, and other important metadata.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeClusterResult) -> dict:
    out: dict = {}
    if "cluster_metadata" in value:
        import aws_sdk_snowball.types.cluster_metadata

        out["ClusterMetadata"] = (
            aws_sdk_snowball.types.cluster_metadata.serialize_aws_json_1_1(
                value["cluster_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeClusterResult:
    out: DescribeClusterResult = {}  # type: ignore[typeddict-item]
    if "ClusterMetadata" in data:
        import aws_sdk_snowball.types.cluster_metadata

        out["cluster_metadata"] = (
            aws_sdk_snowball.types.cluster_metadata.deserialize_aws_json_1_1(
                data["ClusterMetadata"]
            )
        )
    return out
