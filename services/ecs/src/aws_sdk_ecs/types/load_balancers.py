"""Generated from Smithy shape ``com.amazonaws.ecs#LoadBalancers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.load_balancer

LoadBalancers: TypeAlias = list["aws_sdk_ecs.types.load_balancer.LoadBalancer"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LoadBalancers) -> list:
    import aws_sdk_ecs.types.load_balancer

    out: list = []
    for item in value:
        out.append(aws_sdk_ecs.types.load_balancer.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LoadBalancers:
    import aws_sdk_ecs.types.load_balancer

    out: LoadBalancers = []
    for item in data:
        out.append(aws_sdk_ecs.types.load_balancer.deserialize_aws_json_1_1(item))
    return out
