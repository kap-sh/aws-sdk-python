"""Generated from Smithy shape ``com.amazonaws.autoscaling#LocalStorageType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling._protocol.xml import Element
from aws_sdk_auto_scaling.errors import DeserializationError

LocalStorageType: TypeAlias = Literal[
    "hdd",
    "ssd",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "hdd",
        "ssd",
    )
)


def to_query_text(value: LocalStorageType) -> str:
    return value


def from_query_text(text: str) -> LocalStorageType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown LocalStorageType value: {text!r}")
    return cast(LocalStorageType, text)


def serialize_query(
    value: LocalStorageType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> LocalStorageType:
    return from_query_text(el.text or "")
