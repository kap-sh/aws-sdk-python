"""Generated from Smithy shape ``com.amazonaws.cloudformation#GeneratedTemplateStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

GeneratedTemplateStatus: TypeAlias = Literal[
    "CREATE_PENDING",
    "UPDATE_PENDING",
    "DELETE_PENDING",
    "CREATE_IN_PROGRESS",
    "UPDATE_IN_PROGRESS",
    "DELETE_IN_PROGRESS",
    "FAILED",
    "COMPLETE",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATE_PENDING",
        "UPDATE_PENDING",
        "DELETE_PENDING",
        "CREATE_IN_PROGRESS",
        "UPDATE_IN_PROGRESS",
        "DELETE_IN_PROGRESS",
        "FAILED",
        "COMPLETE",
    )
)


def to_query_text(value: GeneratedTemplateStatus) -> str:
    return value


def from_query_text(text: str) -> GeneratedTemplateStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown GeneratedTemplateStatus value: {text!r}")
    return cast(GeneratedTemplateStatus, text)


def serialize_query(
    value: GeneratedTemplateStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> GeneratedTemplateStatus:
    return from_query_text(el.text or "")
