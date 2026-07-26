"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEksClusterLoggingDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_eks_cluster_logging_cluster_logging_list


class AwsEksClusterLoggingDetails(TypedDict, closed=True):
    cluster_logging: NotRequired[
        "capo_securityhub.types.aws_eks_cluster_logging_cluster_logging_list.AwsEksClusterLoggingClusterLoggingList"
    ]
    """<p>Cluster logging configurations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsEksClusterLoggingDetails) -> dict:
    out: dict = {}
    if "cluster_logging" in value:
        import capo_securityhub.types.aws_eks_cluster_logging_cluster_logging_list

        out["ClusterLogging"] = (
            capo_securityhub.types.aws_eks_cluster_logging_cluster_logging_list.serialize_json(
                value["cluster_logging"]
            )
        )
    return out


def deserialize_json(data: dict) -> AwsEksClusterLoggingDetails:
    out: AwsEksClusterLoggingDetails = {}  # type: ignore[typeddict-item]
    if "ClusterLogging" in data:
        import capo_securityhub.types.aws_eks_cluster_logging_cluster_logging_list

        out["cluster_logging"] = (
            capo_securityhub.types.aws_eks_cluster_logging_cluster_logging_list.deserialize_json(
                data["ClusterLogging"]
            )
        )
    return out
