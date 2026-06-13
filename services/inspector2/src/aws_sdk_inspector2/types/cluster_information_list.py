"""Generated from Smithy shape ``com.amazonaws.inspector2#ClusterInformationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cluster_information

ClusterInformationList: TypeAlias = list[
    "aws_sdk_inspector2.types.cluster_information.ClusterInformation"
]


# --- restJson1 ser/de ---
def serialize_json(value: ClusterInformationList) -> list:
    import aws_sdk_inspector2.types.cluster_information

    out: list = []
    for item in value:
        out.append(aws_sdk_inspector2.types.cluster_information.serialize_json(item))
    return out


def deserialize_json(data: list) -> ClusterInformationList:
    import aws_sdk_inspector2.types.cluster_information

    out: ClusterInformationList = []
    for item in data:
        out.append(aws_sdk_inspector2.types.cluster_information.deserialize_json(item))
    return out
