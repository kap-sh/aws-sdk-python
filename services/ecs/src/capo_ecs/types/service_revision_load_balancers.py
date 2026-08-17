"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceRevisionLoadBalancers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.service_revision_load_balancer

ServiceRevisionLoadBalancers: TypeAlias = list[
    "capo_ecs.types.service_revision_load_balancer.ServiceRevisionLoadBalancer"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceRevisionLoadBalancers) -> list:
    import capo_ecs.types.service_revision_load_balancer

    out: list = []
    for item in value:
        out.append(
            capo_ecs.types.service_revision_load_balancer.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ServiceRevisionLoadBalancers:
    import capo_ecs.types.service_revision_load_balancer

    out: ServiceRevisionLoadBalancers = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_ecs.types.service_revision_load_balancer.deserialize_aws_json_1_1(item)
        )
    return out
