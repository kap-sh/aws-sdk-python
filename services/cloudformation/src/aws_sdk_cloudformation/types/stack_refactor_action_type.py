"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackRefactorActionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

StackRefactorActionType: TypeAlias = Literal[
    "MOVE",
    "CREATE",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MOVE",
        "CREATE",
    )
)


def to_query_text(value: StackRefactorActionType) -> str:
    return value


def from_query_text(text: str) -> StackRefactorActionType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown StackRefactorActionType value: {text!r}")
    return cast(StackRefactorActionType, text)


def serialize_query(
    value: StackRefactorActionType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> StackRefactorActionType:
    return from_query_text(el.text or "")
