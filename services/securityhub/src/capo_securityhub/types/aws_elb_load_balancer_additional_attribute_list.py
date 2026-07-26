"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElbLoadBalancerAdditionalAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_elb_load_balancer_additional_attribute

AwsElbLoadBalancerAdditionalAttributeList: TypeAlias = list[
    "capo_securityhub.types.aws_elb_load_balancer_additional_attribute.AwsElbLoadBalancerAdditionalAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsElbLoadBalancerAdditionalAttributeList) -> list:
    import capo_securityhub.types.aws_elb_load_balancer_additional_attribute

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_elb_load_balancer_additional_attribute.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsElbLoadBalancerAdditionalAttributeList:
    import capo_securityhub.types.aws_elb_load_balancer_additional_attribute

    out: AwsElbLoadBalancerAdditionalAttributeList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_elb_load_balancer_additional_attribute.deserialize_json(
                item
            )
        )
    return out
