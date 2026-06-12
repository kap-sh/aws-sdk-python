"""Generated from Smithy shape ``com.amazonaws.autoscaling#RetryStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling._protocol.xml import Element
from aws_sdk_auto_scaling.errors import DeserializationError

RetryStrategy: TypeAlias = Literal[
    "retry-with-group-configuration",
    "none",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "retry-with-group-configuration",
        "none",
    )
)


def to_query_text(value: RetryStrategy) -> str:
    return value


def from_query_text(text: str) -> RetryStrategy:
    if text not in _VALUES:
        raise DeserializationError(f"unknown RetryStrategy value: {text!r}")
    return cast(RetryStrategy, text)


def serialize_query(
    value: RetryStrategy, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> RetryStrategy:
    return from_query_text(el.text or "")
