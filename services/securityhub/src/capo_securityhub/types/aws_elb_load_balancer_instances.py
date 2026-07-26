"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElbLoadBalancerInstances``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_elb_load_balancer_instance

AwsElbLoadBalancerInstances: TypeAlias = list[
    "capo_securityhub.types.aws_elb_load_balancer_instance.AwsElbLoadBalancerInstance"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsElbLoadBalancerInstances) -> list:
    import capo_securityhub.types.aws_elb_load_balancer_instance

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_elb_load_balancer_instance.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AwsElbLoadBalancerInstances:
    import capo_securityhub.types.aws_elb_load_balancer_instance

    out: AwsElbLoadBalancerInstances = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_elb_load_balancer_instance.deserialize_json(item)
        )
    return out
