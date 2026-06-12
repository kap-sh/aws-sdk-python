"""Generated from Smithy shape ``com.amazonaws.autoscaling#RefreshStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling._protocol.xml import Element
from aws_sdk_auto_scaling.errors import DeserializationError

RefreshStrategy: TypeAlias = Literal[
    "Rolling",
    "ReplaceRootVolume",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Rolling",
        "ReplaceRootVolume",
    )
)


def to_query_text(value: RefreshStrategy) -> str:
    return value


def from_query_text(text: str) -> RefreshStrategy:
    if text not in _VALUES:
        raise DeserializationError(f"unknown RefreshStrategy value: {text!r}")
    return cast(RefreshStrategy, text)


def serialize_query(
    value: RefreshStrategy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> RefreshStrategy:
    return from_query_text(el.text or "")
