"""Generated from Smithy shape ``com.amazonaws.elasticache#ClusterMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticache._protocol.xml import Element
from aws_sdk_elasticache.errors import DeserializationError

ClusterMode: TypeAlias = Literal[
    "enabled",
    "disabled",
    "compatible",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "enabled",
        "disabled",
        "compatible",
    )
)


def to_query_text(value: ClusterMode) -> str:
    return value


def from_query_text(text: str) -> ClusterMode:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ClusterMode value: {text!r}")
    return cast(ClusterMode, text)


def serialize_query(
    value: ClusterMode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ClusterMode:
    return from_query_text(el.text or "")
