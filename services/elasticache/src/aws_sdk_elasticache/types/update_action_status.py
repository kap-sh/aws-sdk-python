"""Generated from Smithy shape ``com.amazonaws.elasticache#UpdateActionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticache._protocol.xml import Element
from aws_sdk_elasticache.errors import DeserializationError

UpdateActionStatus: TypeAlias = Literal[
    "not-applied",
    "waiting-to-start",
    "in-progress",
    "stopping",
    "stopped",
    "complete",
    "scheduling",
    "scheduled",
    "not-applicable",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "not-applied",
        "waiting-to-start",
        "in-progress",
        "stopping",
        "stopped",
        "complete",
        "scheduling",
        "scheduled",
        "not-applicable",
    )
)


def to_query_text(value: UpdateActionStatus) -> str:
    return value


def from_query_text(text: str) -> UpdateActionStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown UpdateActionStatus value: {text!r}")
    return cast(UpdateActionStatus, text)


def serialize_query(
    value: UpdateActionStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> UpdateActionStatus:
    return from_query_text(el.text or "")
