"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#SslPolicyNames``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_load_balancing_v2.types.ssl_policy_name

SslPolicyNames: TypeAlias = list[
    "capo_elastic_load_balancing_v2.types.ssl_policy_name.SslPolicyName"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: SslPolicyNames, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> SslPolicyNames:
    out: SslPolicyNames = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: SslPolicyNames, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> SslPolicyNames:
    out: SslPolicyNames = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
