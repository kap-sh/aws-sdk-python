"""Generated from Smithy shape ``com.amazonaws.cloudformation#AccountGateStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

AccountGateStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "FAILED",
    "SKIPPED",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SUCCEEDED",
        "FAILED",
        "SKIPPED",
    )
)


def to_query_text(value: AccountGateStatus) -> str:
    return value


def from_query_text(text: str) -> AccountGateStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown AccountGateStatus value: {text!r}")
    return cast(AccountGateStatus, text)


def serialize_query(
    value: AccountGateStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AccountGateStatus:
    return from_query_text(el.text or "")
