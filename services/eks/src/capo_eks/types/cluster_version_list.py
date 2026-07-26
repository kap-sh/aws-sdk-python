"""Generated from Smithy shape ``com.amazonaws.eks#ClusterVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eks.types.cluster_version_information

ClusterVersionList: TypeAlias = list[
    "capo_eks.types.cluster_version_information.ClusterVersionInformation"
]


# --- restJson1 ser/de ---
def serialize_json(value: ClusterVersionList) -> list:
    import capo_eks.types.cluster_version_information

    out: list = []
    for item in value:
        out.append(capo_eks.types.cluster_version_information.serialize_json(item))
    return out


def deserialize_json(data: list) -> ClusterVersionList:
    import capo_eks.types.cluster_version_information

    out: ClusterVersionList = []
    for item in data:
        out.append(capo_eks.types.cluster_version_information.deserialize_json(item))
    return out
