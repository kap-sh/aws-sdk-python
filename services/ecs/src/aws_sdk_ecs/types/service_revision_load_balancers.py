"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceRevisionLoadBalancers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.service_revision_load_balancer

ServiceRevisionLoadBalancers: TypeAlias = list[
    "aws_sdk_ecs.types.service_revision_load_balancer.ServiceRevisionLoadBalancer"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceRevisionLoadBalancers) -> list:
    import aws_sdk_ecs.types.service_revision_load_balancer

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ecs.types.service_revision_load_balancer.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ServiceRevisionLoadBalancers:
    import aws_sdk_ecs.types.service_revision_load_balancer

    out: ServiceRevisionLoadBalancers = []
    for item in data:
        out.append(
            aws_sdk_ecs.types.service_revision_load_balancer.deserialize_aws_json_1_1(
                item
            )
        )
    return out
