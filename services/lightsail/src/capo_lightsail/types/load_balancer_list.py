"""Generated from Smithy shape ``com.amazonaws.lightsail#LoadBalancerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.load_balancer

LoadBalancerList: TypeAlias = list["capo_lightsail.types.load_balancer.LoadBalancer"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LoadBalancerList) -> list:
    import capo_lightsail.types.load_balancer

    out: list = []
    for item in value:
        out.append(capo_lightsail.types.load_balancer.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> LoadBalancerList:
    import capo_lightsail.types.load_balancer

    out: LoadBalancerList = []
    for item in data:
        out.append(capo_lightsail.types.load_balancer.deserialize_aws_json_1_1(item))
    return out
