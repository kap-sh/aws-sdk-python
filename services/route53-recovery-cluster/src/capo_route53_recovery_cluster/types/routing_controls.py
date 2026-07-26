"""Generated from Smithy shape ``com.amazonaws.route53recoverycluster#RoutingControls``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_route53_recovery_cluster.types.routing_control

RoutingControls: TypeAlias = list[
    "capo_route53_recovery_cluster.types.routing_control.RoutingControl"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RoutingControls) -> list:
    import capo_route53_recovery_cluster.types.routing_control

    out: list = []
    for item in value:
        out.append(
            capo_route53_recovery_cluster.types.routing_control.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> RoutingControls:
    import capo_route53_recovery_cluster.types.routing_control

    out: RoutingControls = []
    for item in data:
        out.append(
            capo_route53_recovery_cluster.types.routing_control.deserialize_aws_json_1_0(
                item
            )
        )
    return out
