"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#__listOfCluster``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_route53_recovery_control_config.types.cluster

__listOfCluster: TypeAlias = list[
    "aws_sdk_route53_recovery_control_config.types.cluster.Cluster"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfCluster) -> list:
    import aws_sdk_route53_recovery_control_config.types.cluster

    out: list = []
    for item in value:
        out.append(
            aws_sdk_route53_recovery_control_config.types.cluster.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> __listOfCluster:
    import aws_sdk_route53_recovery_control_config.types.cluster

    out: __listOfCluster = []
    for item in data:
        out.append(
            aws_sdk_route53_recovery_control_config.types.cluster.deserialize_json(item)
        )
    return out
