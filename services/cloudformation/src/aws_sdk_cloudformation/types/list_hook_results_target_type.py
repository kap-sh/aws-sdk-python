"""Generated from Smithy shape ``com.amazonaws.cloudformation#ListHookResultsTargetType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

ListHookResultsTargetType: TypeAlias = Literal[
    "CHANGE_SET",
    "STACK",
    "RESOURCE",
    "CLOUD_CONTROL",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CHANGE_SET",
        "STACK",
        "RESOURCE",
        "CLOUD_CONTROL",
    )
)


def to_query_text(value: ListHookResultsTargetType) -> str:
    return value


def from_query_text(text: str) -> ListHookResultsTargetType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ListHookResultsTargetType value: {text!r}")
    return cast(ListHookResultsTargetType, text)


def serialize_query(
    value: ListHookResultsTargetType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ListHookResultsTargetType:
    return from_query_text(el.text or "")
