"""Generated from Smithy shape ``com.amazonaws.rds#ExportSourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rds._protocol.xml import Element
from aws_sdk_rds.errors import DeserializationError

ExportSourceType: TypeAlias = Literal[
    "SNAPSHOT",
    "CLUSTER",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SNAPSHOT",
        "CLUSTER",
    )
)


def to_query_text(value: ExportSourceType) -> str:
    return value


def from_query_text(text: str) -> ExportSourceType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ExportSourceType value: {text!r}")
    return cast(ExportSourceType, text)


def serialize_query(
    value: ExportSourceType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ExportSourceType:
    return from_query_text(el.text or "")
