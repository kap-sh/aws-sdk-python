"""Generated from Smithy shape ``com.amazonaws.iam#permissionCheckResultType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iam._protocol.xml import Element
from aws_sdk_iam.errors import DeserializationError

permissionCheckResultType: TypeAlias = Literal[
    "ALLOWED",
    "DENIED",
    "UNSURE",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ALLOWED",
        "DENIED",
        "UNSURE",
    )
)


def to_query_text(value: permissionCheckResultType) -> str:
    return value


def from_query_text(text: str) -> permissionCheckResultType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown permissionCheckResultType value: {text!r}")
    return cast(permissionCheckResultType, text)


def serialize_query(
    value: permissionCheckResultType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> permissionCheckResultType:
    return from_query_text(el.text or "")
