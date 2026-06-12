"""Generated from Smithy shape ``com.amazonaws.redshift#OperatorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import DeserializationError

OperatorType: TypeAlias = Literal[
    "eq",
    "lt",
    "gt",
    "le",
    "ge",
    "in",
    "between",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "eq",
        "lt",
        "gt",
        "le",
        "ge",
        "in",
        "between",
    )
)


def to_query_text(value: OperatorType) -> str:
    return value


def from_query_text(text: str) -> OperatorType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown OperatorType value: {text!r}")
    return cast(OperatorType, text)


def serialize_query(
    value: OperatorType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> OperatorType:
    return from_query_text(el.text or "")
