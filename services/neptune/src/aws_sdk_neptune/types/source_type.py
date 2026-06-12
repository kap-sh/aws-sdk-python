"""Generated from Smithy shape ``com.amazonaws.neptune#SourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_neptune._protocol.xml import Element
from aws_sdk_neptune.errors import DeserializationError

SourceType: TypeAlias = Literal[
    "db-instance",
    "db-parameter-group",
    "db-security-group",
    "db-snapshot",
    "db-cluster",
    "db-cluster-snapshot",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "db-instance",
        "db-parameter-group",
        "db-security-group",
        "db-snapshot",
        "db-cluster",
        "db-cluster-snapshot",
    )
)


def to_query_text(value: SourceType) -> str:
    return value


def from_query_text(text: str) -> SourceType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown SourceType value: {text!r}")
    return cast(SourceType, text)


def serialize_query(
    value: SourceType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> SourceType:
    return from_query_text(el.text or "")
