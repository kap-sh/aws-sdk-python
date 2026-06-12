"""Generated from Smithy shape ``com.amazonaws.elasticache#PendingAutomaticFailoverStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticache._protocol.xml import Element
from aws_sdk_elasticache.errors import DeserializationError

PendingAutomaticFailoverStatus: TypeAlias = Literal[
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


def to_query_text(value: PendingAutomaticFailoverStatus) -> str:
    return value


def from_query_text(text: str) -> PendingAutomaticFailoverStatus:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown PendingAutomaticFailoverStatus value: {text!r}"
        )
    return cast(PendingAutomaticFailoverStatus, text)


def serialize_query(
    value: PendingAutomaticFailoverStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> PendingAutomaticFailoverStatus:
    return from_query_text(el.text or "")
