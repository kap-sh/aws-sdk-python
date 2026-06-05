"""Generated from Smithy shape ``com.amazonaws.ec2#ClassicLoadBalancers``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.classic_load_balancer

ClassicLoadBalancers: TypeAlias = list[
    "aws_sdk_ec2.types.classic_load_balancer.ClassicLoadBalancer"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ClassicLoadBalancers, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.classic_load_balancer

        aws_sdk_ec2.types.classic_load_balancer.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> ClassicLoadBalancers:
    import aws_sdk_ec2.types.classic_load_balancer

    out: ClassicLoadBalancers = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.classic_load_balancer.deserialize_ec2_query(child))
    return out
