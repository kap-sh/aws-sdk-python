"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElbv2LoadBalancerAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_elbv2_load_balancer_attribute

AwsElbv2LoadBalancerAttributes: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_elbv2_load_balancer_attribute.AwsElbv2LoadBalancerAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsElbv2LoadBalancerAttributes) -> list:
    import aws_sdk_securityhub.types.aws_elbv2_load_balancer_attribute

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_elbv2_load_balancer_attribute.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsElbv2LoadBalancerAttributes:
    import aws_sdk_securityhub.types.aws_elbv2_load_balancer_attribute

    out: AwsElbv2LoadBalancerAttributes = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_elbv2_load_balancer_attribute.deserialize_json(
                item
            )
        )
    return out
