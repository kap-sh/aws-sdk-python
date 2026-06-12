"""Generated from Smithy shape ``com.amazonaws.rds#TargetRole``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rds._protocol.xml import Element
from aws_sdk_rds.errors import DeserializationError

TargetRole: TypeAlias = Literal[
    "READ_WRITE",
    "READ_ONLY",
    "UNKNOWN",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "READ_WRITE",
        "READ_ONLY",
        "UNKNOWN",
    )
)


def to_query_text(value: TargetRole) -> str:
    return value


def from_query_text(text: str) -> TargetRole:
    if text not in _VALUES:
        raise DeserializationError(f"unknown TargetRole value: {text!r}")
    return cast(TargetRole, text)


def serialize_query(
    value: TargetRole, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> TargetRole:
    return from_query_text(el.text or "")
