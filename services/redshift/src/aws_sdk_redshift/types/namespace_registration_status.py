"""Generated from Smithy shape ``com.amazonaws.redshift#NamespaceRegistrationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import DeserializationError

NamespaceRegistrationStatus: TypeAlias = Literal[
    "Registering",
    "Deregistering",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Registering",
        "Deregistering",
    )
)


def to_query_text(value: NamespaceRegistrationStatus) -> str:
    return value


def from_query_text(text: str) -> NamespaceRegistrationStatus:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown NamespaceRegistrationStatus value: {text!r}"
        )
    return cast(NamespaceRegistrationStatus, text)


def serialize_query(
    value: NamespaceRegistrationStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> NamespaceRegistrationStatus:
    return from_query_text(el.text or "")
