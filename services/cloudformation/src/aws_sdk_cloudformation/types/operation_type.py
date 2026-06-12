"""Generated from Smithy shape ``com.amazonaws.cloudformation#OperationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

OperationType: TypeAlias = Literal[
    "CREATE_STACK",
    "UPDATE_STACK",
    "DELETE_STACK",
    "CONTINUE_ROLLBACK",
    "ROLLBACK",
    "CREATE_CHANGESET",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_STACK",
        "UPDATE_STACK",
        "DELETE_STACK",
        "CONTINUE_ROLLBACK",
        "ROLLBACK",
        "CREATE_CHANGESET",
    )
)


def to_query_text(value: OperationType) -> str:
    return value


def from_query_text(text: str) -> OperationType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown OperationType value: {text!r}")
    return cast(OperationType, text)


def serialize_query(
    value: OperationType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> OperationType:
    return from_query_text(el.text or "")
