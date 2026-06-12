"""Generated from Smithy shape ``com.amazonaws.cloudformation#StackSetOperationAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

StackSetOperationAction: TypeAlias = Literal[
    "CREATE",
    "UPDATE",
    "DELETE",
    "DETECT_DRIFT",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE",
        "UPDATE",
        "DELETE",
        "DETECT_DRIFT",
    )
)


def to_query_text(value: StackSetOperationAction) -> str:
    return value


def from_query_text(text: str) -> StackSetOperationAction:
    if text not in _VALUES:
        raise DeserializationError(f"unknown StackSetOperationAction value: {text!r}")
    return cast(StackSetOperationAction, text)


def serialize_query(
    value: StackSetOperationAction, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> StackSetOperationAction:
    return from_query_text(el.text or "")
