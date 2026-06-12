"""Generated from Smithy shape ``com.amazonaws.emr#ClusterStateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_emr.types.cluster_state

ClusterStateList: TypeAlias = list["aws_sdk_emr.types.cluster_state.ClusterState"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterStateList) -> list:
    import aws_sdk_emr.types.cluster_state

    out: list = []
    for item in value:
        out.append(aws_sdk_emr.types.cluster_state.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ClusterStateList:
    import aws_sdk_emr.types.cluster_state

    out: ClusterStateList = []
    for item in data:
        out.append(aws_sdk_emr.types.cluster_state.deserialize_aws_json_1_1(item))
    return out
