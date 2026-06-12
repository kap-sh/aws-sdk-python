"""Generated from Smithy shape ``com.amazonaws.cloudformation#EvaluationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

EvaluationType: TypeAlias = Literal[
    "Static",
    "Dynamic",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Static",
        "Dynamic",
    )
)


def to_query_text(value: EvaluationType) -> str:
    return value


def from_query_text(text: str) -> EvaluationType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown EvaluationType value: {text!r}")
    return cast(EvaluationType, text)


def serialize_query(
    value: EvaluationType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> EvaluationType:
    return from_query_text(el.text or "")
