"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEksClusterLoggingClusterLoggingList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_eks_cluster_logging_cluster_logging_details

AwsEksClusterLoggingClusterLoggingList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_eks_cluster_logging_cluster_logging_details.AwsEksClusterLoggingClusterLoggingDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEksClusterLoggingClusterLoggingList) -> list:
    import aws_sdk_securityhub.types.aws_eks_cluster_logging_cluster_logging_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_eks_cluster_logging_cluster_logging_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEksClusterLoggingClusterLoggingList:
    import aws_sdk_securityhub.types.aws_eks_cluster_logging_cluster_logging_details

    out: AwsEksClusterLoggingClusterLoggingList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_eks_cluster_logging_cluster_logging_details.deserialize_json(
                item
            )
        )
    return out
