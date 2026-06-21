"""Generated from Smithy shape ``com.amazonaws.redshift#NamespaceRegistrationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_redshift._protocol.xml import Element

NamespaceRegistrationStatus: TypeAlias = Literal[
    "Registering",
    "Deregistering",
]


# --- awsQuery ser/de ---
def to_query_text(value: NamespaceRegistrationStatus) -> str:
    return value


def from_query_text(text: str) -> NamespaceRegistrationStatus:
    return cast(NamespaceRegistrationStatus, text)


def serialize_query(
    value: NamespaceRegistrationStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> NamespaceRegistrationStatus:
    return from_query_text(el.text or "")
