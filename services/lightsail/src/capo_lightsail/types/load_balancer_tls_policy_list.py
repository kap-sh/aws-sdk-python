"""Generated from Smithy shape ``com.amazonaws.lightsail#LoadBalancerTlsPolicyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lightsail.types.load_balancer_tls_policy

LoadBalancerTlsPolicyList: TypeAlias = list[
    "capo_lightsail.types.load_balancer_tls_policy.LoadBalancerTlsPolicy"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LoadBalancerTlsPolicyList) -> list:
    import capo_lightsail.types.load_balancer_tls_policy

    out: list = []
    for item in value:
        out.append(
            capo_lightsail.types.load_balancer_tls_policy.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> LoadBalancerTlsPolicyList:
    import capo_lightsail.types.load_balancer_tls_policy

    out: LoadBalancerTlsPolicyList = []
    for item in data:
        out.append(
            capo_lightsail.types.load_balancer_tls_policy.deserialize_aws_json_1_1(item)
        )
    return out
