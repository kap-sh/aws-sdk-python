"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackRefactorActionEntity``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

StackRefactorActionEntity: TypeAlias = Literal[
    "RESOURCE",
    "STACK",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RESOURCE",
        "STACK",
    )
)


def to_query_text(value: StackRefactorActionEntity) -> str:
    return value


def from_query_text(text: str) -> StackRefactorActionEntity:
    if text not in _VALUES:
        raise DeserializationError(f"unknown StackRefactorActionEntity value: {text!r}")
    return cast(StackRefactorActionEntity, text)


def serialize_query(
    value: StackRefactorActionEntity, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> StackRefactorActionEntity:
    return from_query_text(el.text or "")
