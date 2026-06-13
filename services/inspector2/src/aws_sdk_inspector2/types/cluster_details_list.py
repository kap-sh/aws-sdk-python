"""Generated from Smithy shape ``com.amazonaws.inspector2#ClusterDetailsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.cluster_details

ClusterDetailsList: TypeAlias = list[
    "aws_sdk_inspector2.types.cluster_details.ClusterDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: ClusterDetailsList) -> list:
    import aws_sdk_inspector2.types.cluster_details

    out: list = []
    for item in value:
        out.append(aws_sdk_inspector2.types.cluster_details.serialize_json(item))
    return out


def deserialize_json(data: list) -> ClusterDetailsList:
    import aws_sdk_inspector2.types.cluster_details

    out: ClusterDetailsList = []
    for item in data:
        out.append(aws_sdk_inspector2.types.cluster_details.deserialize_json(item))
    return out
