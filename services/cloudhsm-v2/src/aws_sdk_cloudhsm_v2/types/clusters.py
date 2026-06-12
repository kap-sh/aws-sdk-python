"""Generated from Smithy shape ``com.amazonaws.cloudhsmv2#Clusters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudhsm_v2.types.cluster

Clusters: TypeAlias = list["aws_sdk_cloudhsm_v2.types.cluster.Cluster"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Clusters) -> list:
    import aws_sdk_cloudhsm_v2.types.cluster

    out: list = []
    for item in value:
        out.append(aws_sdk_cloudhsm_v2.types.cluster.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Clusters:
    import aws_sdk_cloudhsm_v2.types.cluster

    out: Clusters = []
    for item in data:
        out.append(aws_sdk_cloudhsm_v2.types.cluster.deserialize_aws_json_1_1(item))
    return out
