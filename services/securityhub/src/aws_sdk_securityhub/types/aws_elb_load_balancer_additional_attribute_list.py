"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsElbLoadBalancerAdditionalAttributeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_elb_load_balancer_additional_attribute

AwsElbLoadBalancerAdditionalAttributeList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_elb_load_balancer_additional_attribute.AwsElbLoadBalancerAdditionalAttribute"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsElbLoadBalancerAdditionalAttributeList) -> list:
    import aws_sdk_securityhub.types.aws_elb_load_balancer_additional_attribute

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_elb_load_balancer_additional_attribute.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsElbLoadBalancerAdditionalAttributeList:
    import aws_sdk_securityhub.types.aws_elb_load_balancer_additional_attribute

    out: AwsElbLoadBalancerAdditionalAttributeList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_elb_load_balancer_additional_attribute.deserialize_json(
                item
            )
        )
    return out
