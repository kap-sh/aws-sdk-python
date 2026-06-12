"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#RevocationIds``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elastic_load_balancing_v2.types.revocation_id

RevocationIds: TypeAlias = list[
    "aws_sdk_elastic_load_balancing_v2.types.revocation_id.RevocationId"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: RevocationIds, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> RevocationIds:
    out: RevocationIds = []
    for child in el.findall("member"):
        out.append(int(child.text or ""))
    return out


def serialize_query_flat(
    value: RevocationIds, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> RevocationIds:
    out: RevocationIds = []
    for child in parent.findall(tag):
        out.append(int(child.text or ""))
    return out
