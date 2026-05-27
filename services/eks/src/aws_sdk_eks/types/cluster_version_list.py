"""Generated from Smithy shape ``com.amazonaws.eks#ClusterVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_eks.types.cluster_version_information

ClusterVersionList: TypeAlias = list[
    "aws_sdk_eks.types.cluster_version_information.ClusterVersionInformation"
]


# --- restJson1 ser/de ---
def serialize_json(value: ClusterVersionList) -> list:
    import aws_sdk_eks.types.cluster_version_information

    out: list = []
    for item in value:
        out.append(aws_sdk_eks.types.cluster_version_information.serialize_json(item))
    return out


def deserialize_json(data: list) -> ClusterVersionList:
    import aws_sdk_eks.types.cluster_version_information

    out: ClusterVersionList = []
    for item in data:
        out.append(aws_sdk_eks.types.cluster_version_information.deserialize_json(item))
    return out
