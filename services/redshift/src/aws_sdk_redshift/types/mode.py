"""Generated from Smithy shape ``com.amazonaws.redshift#Mode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import DeserializationError

Mode: TypeAlias = Literal[
    "standard",
    "high-performance",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "standard",
        "high-performance",
    )
)


def to_query_text(value: Mode) -> str:
    return value


def from_query_text(text: str) -> Mode:
    if text not in _VALUES:
        raise DeserializationError(f"unknown Mode value: {text!r}")
    return cast(Mode, text)


def serialize_query(value: Mode, pairs: list[tuple[str, str]], prefix: str) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> Mode:
    return from_query_text(el.text or "")
