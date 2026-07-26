"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElbv2LoadBalancerAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_elbv2_load_balancer_attribute

AwsElbv2LoadBalancerAttributes: TypeAlias = list[
    "capo_securityhub.types.aws_elbv2_load_balancer_attribute.AwsElbv2LoadBalancerAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsElbv2LoadBalancerAttributes) -> list:
    import capo_securityhub.types.aws_elbv2_load_balancer_attribute

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_elbv2_load_balancer_attribute.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsElbv2LoadBalancerAttributes:
    import capo_securityhub.types.aws_elbv2_load_balancer_attribute

    out: AwsElbv2LoadBalancerAttributes = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_elbv2_load_balancer_attribute.deserialize_json(
                item
            )
        )
    return out
