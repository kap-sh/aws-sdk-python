"""Generated from Smithy shape ``com.amazonaws.inspector2#ClusterInformationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.cluster_information

ClusterInformationList: TypeAlias = list[
    "capo_inspector2.types.cluster_information.ClusterInformation"
]


# --- restJson1 ser/de ---
def serialize_json(value: ClusterInformationList) -> list:
    import capo_inspector2.types.cluster_information

    out: list = []
    for item in value:
        out.append(capo_inspector2.types.cluster_information.serialize_json(item))
    return out


def deserialize_json(data: list) -> ClusterInformationList:
    import capo_inspector2.types.cluster_information

    out: ClusterInformationList = []
    for item in data:
        out.append(capo_inspector2.types.cluster_information.deserialize_json(item))
    return out
