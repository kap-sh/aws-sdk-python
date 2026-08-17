"""Generated from Smithy shape ``com.amazonaws.ecs#LoadBalancers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.load_balancer

LoadBalancers: TypeAlias = list["capo_ecs.types.load_balancer.LoadBalancer"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LoadBalancers) -> list:
    import capo_ecs.types.load_balancer

    out: list = []
    for item in value:
        out.append(capo_ecs.types.load_balancer.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LoadBalancers:
    import capo_ecs.types.load_balancer

    out: LoadBalancers = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.load_balancer.deserialize_aws_json_1_1(item))
    return out
