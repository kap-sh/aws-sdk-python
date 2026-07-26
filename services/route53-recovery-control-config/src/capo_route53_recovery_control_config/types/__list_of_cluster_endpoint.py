"""Generated from Smithy shape ``com.amazonaws.route53recoverycontrolconfig#__listOfClusterEndpoint``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53_recovery_control_config.types.cluster_endpoint

__listOfClusterEndpoint: TypeAlias = list[
    "capo_route53_recovery_control_config.types.cluster_endpoint.ClusterEndpoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfClusterEndpoint) -> list:
    import capo_route53_recovery_control_config.types.cluster_endpoint

    out: list = []
    for item in value:
        out.append(
            capo_route53_recovery_control_config.types.cluster_endpoint.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> __listOfClusterEndpoint:
    import capo_route53_recovery_control_config.types.cluster_endpoint

    out: __listOfClusterEndpoint = []
    for item in data:
        out.append(
            capo_route53_recovery_control_config.types.cluster_endpoint.deserialize_json(
                item
            )
        )
    return out
