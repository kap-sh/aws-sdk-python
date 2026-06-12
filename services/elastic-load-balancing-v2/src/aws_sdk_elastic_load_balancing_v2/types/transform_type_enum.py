"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#TransformTypeEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element
from aws_sdk_elastic_load_balancing_v2.errors import DeserializationError

TransformTypeEnum: TypeAlias = Literal[
    "host-header-rewrite",
    "url-rewrite",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "host-header-rewrite",
        "url-rewrite",
    )
)


def to_query_text(value: TransformTypeEnum) -> str:
    return value


def from_query_text(text: str) -> TransformTypeEnum:
    if text not in _VALUES:
        raise DeserializationError(f"unknown TransformTypeEnum value: {text!r}")
    return cast(TransformTypeEnum, text)


def serialize_query(
    value: TransformTypeEnum, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> TransformTypeEnum:
    return from_query_text(el.text or "")
