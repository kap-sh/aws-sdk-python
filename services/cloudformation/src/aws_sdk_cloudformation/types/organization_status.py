"""Generated from Smithy shape ``com.amazonaws.cloudformation#OrganizationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element
from aws_sdk_cloudformation.errors import DeserializationError

OrganizationStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "DISABLED_PERMANENTLY",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
        "DISABLED_PERMANENTLY",
    )
)


def to_query_text(value: OrganizationStatus) -> str:
    return value


def from_query_text(text: str) -> OrganizationStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown OrganizationStatus value: {text!r}")
    return cast(OrganizationStatus, text)


def serialize_query(
    value: OrganizationStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> OrganizationStatus:
    return from_query_text(el.text or "")
