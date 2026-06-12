"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#RedirectActionStatusCodeEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element
from aws_sdk_elastic_load_balancing_v2.errors import DeserializationError

RedirectActionStatusCodeEnum: TypeAlias = Literal[
    "HTTP_301",
    "HTTP_302",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HTTP_301",
        "HTTP_302",
    )
)


def to_query_text(value: RedirectActionStatusCodeEnum) -> str:
    return value


def from_query_text(text: str) -> RedirectActionStatusCodeEnum:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown RedirectActionStatusCodeEnum value: {text!r}"
        )
    return cast(RedirectActionStatusCodeEnum, text)


def serialize_query(
    value: RedirectActionStatusCodeEnum, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> RedirectActionStatusCodeEnum:
    return from_query_text(el.text or "")
