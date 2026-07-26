"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#RedirectActionStatusCodeEnum``."""

from typing import Literal, TypeAlias, cast

from capo_elastic_load_balancing_v2._protocol.xml import Element

RedirectActionStatusCodeEnum: TypeAlias = Literal[
    "HTTP_301",
    "HTTP_302",
]


# --- awsQuery ser/de ---
def to_query_text(value: RedirectActionStatusCodeEnum) -> str:
    return value


def from_query_text(text: str) -> RedirectActionStatusCodeEnum:
    return cast(RedirectActionStatusCodeEnum, text)


def serialize_query(
    value: RedirectActionStatusCodeEnum, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> RedirectActionStatusCodeEnum:
    return from_query_text(el.text or "")
