"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#LoadBalancerStateEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

LoadBalancerStateEnum: TypeAlias = Literal[
    "active",
    "provisioning",
    "active_impaired",
    "failed",
]


# --- awsQuery ser/de ---
def to_query_text(value: LoadBalancerStateEnum) -> str:
    return value


def from_query_text(text: str) -> LoadBalancerStateEnum:
    return cast(LoadBalancerStateEnum, text)


def serialize_query(
    value: LoadBalancerStateEnum, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> LoadBalancerStateEnum:
    return from_query_text(el.text or "")
