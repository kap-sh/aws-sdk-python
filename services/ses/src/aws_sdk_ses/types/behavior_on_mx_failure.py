"""Generated from Smithy shape ``com.amazonaws.ses#BehaviorOnMXFailure``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

BehaviorOnMXFailure: TypeAlias = Literal[
    "UseDefaultValue",
    "RejectMessage",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UseDefaultValue",
        "RejectMessage",
    )
)


def to_query_text(value: BehaviorOnMXFailure) -> str:
    return value


def from_query_text(text: str) -> BehaviorOnMXFailure:
    if text not in _VALUES:
        raise DeserializationError(f"unknown BehaviorOnMXFailure value: {text!r}")
    return cast(BehaviorOnMXFailure, text)


def serialize_query(
    value: BehaviorOnMXFailure, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> BehaviorOnMXFailure:
    return from_query_text(el.text or "")
