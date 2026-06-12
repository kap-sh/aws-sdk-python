"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#ListenerArns``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.listener_arn

ListenerArns: TypeAlias = list[
    "aws_sdk_elastic_load_balancing_v2.types.listener_arn.ListenerArn"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: ListenerArns, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> ListenerArns:
    out: ListenerArns = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: ListenerArns, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> ListenerArns:
    out: ListenerArns = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
