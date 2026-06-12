"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfClusterAlert``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.cluster_alert

__listOfClusterAlert: TypeAlias = list[
    "aws_sdk_medialive.types.cluster_alert.ClusterAlert"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfClusterAlert) -> list:
    import aws_sdk_medialive.types.cluster_alert

    out: list = []
    for item in value:
        out.append(aws_sdk_medialive.types.cluster_alert.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfClusterAlert:
    import aws_sdk_medialive.types.cluster_alert

    out: __listOfClusterAlert = []
    for item in data:
        out.append(aws_sdk_medialive.types.cluster_alert.deserialize_json(item))
    return out
