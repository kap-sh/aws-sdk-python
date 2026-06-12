"""Generated from Smithy shape ``com.amazonaws.elasticache#MultiAZStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticache._protocol.xml import Element
from aws_sdk_elasticache.errors import DeserializationError

MultiAZStatus: TypeAlias = Literal[
    "enabled",
    "disabled",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "enabled",
        "disabled",
    )
)


def to_query_text(value: MultiAZStatus) -> str:
    return value


def from_query_text(text: str) -> MultiAZStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown MultiAZStatus value: {text!r}")
    return cast(MultiAZStatus, text)


def serialize_query(
    value: MultiAZStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> MultiAZStatus:
    return from_query_text(el.text or "")
