"""Generated from Smithy shape ``com.amazonaws.autoscaling#WarmPoolState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling._protocol.xml import Element
from aws_sdk_auto_scaling.errors import DeserializationError

WarmPoolState: TypeAlias = Literal[
    "Stopped",
    "Running",
    "Hibernated",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Stopped",
        "Running",
        "Hibernated",
    )
)


def to_query_text(value: WarmPoolState) -> str:
    return value


def from_query_text(text: str) -> WarmPoolState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown WarmPoolState value: {text!r}")
    return cast(WarmPoolState, text)


def serialize_query(
    value: WarmPoolState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> WarmPoolState:
    return from_query_text(el.text or "")
