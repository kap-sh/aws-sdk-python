"""Generated from Smithy shape ``com.amazonaws.iam#ContextKeyTypeEnum``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_iam.errors import DeserializationError
from aws_sdk_iam._protocol.xml import Element

ContextKeyTypeEnum: TypeAlias = Literal[
    "string",
    "stringList",
    "numeric",
    "numericList",
    "boolean",
    "booleanList",
    "ip",
    "ipList",
    "binary",
    "binaryList",
    "date",
    "dateList",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "string",
        "stringList",
        "numeric",
        "numericList",
        "boolean",
        "booleanList",
        "ip",
        "ipList",
        "binary",
        "binaryList",
        "date",
        "dateList",
    )
)


def to_query_text(value: ContextKeyTypeEnum) -> str:
    return value


def from_query_text(text: str) -> ContextKeyTypeEnum:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ContextKeyTypeEnum value: {text!r}")
    return cast(ContextKeyTypeEnum, text)


def serialize_query(
    value: ContextKeyTypeEnum, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ContextKeyTypeEnum:
    return from_query_text(el.text or "")
