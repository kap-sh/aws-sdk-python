"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsEcsServiceLoadBalancersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_ecs_service_load_balancers_details

AwsEcsServiceLoadBalancersList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_ecs_service_load_balancers_details.AwsEcsServiceLoadBalancersDetails"
]


# --- restJson1 ser/de ---
def serialize_json(value: AwsEcsServiceLoadBalancersList) -> list:
    import aws_sdk_securityhub.types.aws_ecs_service_load_balancers_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_service_load_balancers_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> AwsEcsServiceLoadBalancersList:
    import aws_sdk_securityhub.types.aws_ecs_service_load_balancers_details

    out: AwsEcsServiceLoadBalancersList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_ecs_service_load_balancers_details.deserialize_json(
                item
            )
        )
    return out
