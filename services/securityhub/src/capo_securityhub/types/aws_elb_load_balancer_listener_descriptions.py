"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElbLoadBalancerListenerDescriptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_elb_load_balancer_listener_description

AwsElbLoadBalancerListenerDescriptions: TypeAlias = list[
    "capo_securityhub.types.aws_elb_load_balancer_listener_description.AwsElbLoadBalancerListenerDescription"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsElbLoadBalancerListenerDescriptions) -> list:
    import capo_securityhub.types.aws_elb_load_balancer_listener_description

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_elb_load_balancer_listener_description.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsElbLoadBalancerListenerDescriptions:
    import capo_securityhub.types.aws_elb_load_balancer_listener_description

    out: AwsElbLoadBalancerListenerDescriptions = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_elb_load_balancer_listener_description.deserialize_json(
                item
            )
        )
    return out
