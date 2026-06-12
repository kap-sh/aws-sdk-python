"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsMskClusterDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_details


class AwsMskClusterDetails(TypedDict):
    cluster_info: NotRequired[
        "aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_details.AwsMskClusterClusterInfoDetails"
    ]
    """<p> Provides information about a cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsMskClusterDetails) -> dict:
    out: dict = {}
    if "cluster_info" in value:
        import aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_details

        out["ClusterInfo"] = (
            aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_details.serialize_json(
                value["cluster_info"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsMskClusterDetails:
    out: AwsMskClusterDetails = {}  # type: ignore[typeddict-item]
    if "ClusterInfo" in data:
        import aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_details

        out["cluster_info"] = (
            aws_sdk_securityhub.types.aws_msk_cluster_cluster_info_details.deserialize_json(
                data["ClusterInfo"]
            )
        )
    return out
