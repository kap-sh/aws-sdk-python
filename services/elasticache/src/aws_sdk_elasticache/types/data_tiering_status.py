"""Generated from Smithy shape ``com.amazonaws.elasticache#DataTieringStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elasticache._protocol.xml import Element
from aws_sdk_elasticache.errors import DeserializationError

DataTieringStatus: TypeAlias = Literal[
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


def to_query_text(value: DataTieringStatus) -> str:
    return value


def from_query_text(text: str) -> DataTieringStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown DataTieringStatus value: {text!r}")
    return cast(DataTieringStatus, text)


def serialize_query(
    value: DataTieringStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> DataTieringStatus:
    return from_query_text(el.text or "")
