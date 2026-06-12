"""Generated from Smithy shape ``com.amazonaws.redshift#PartnerIntegrationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_redshift._protocol.xml import Element
from aws_sdk_redshift.errors import DeserializationError

PartnerIntegrationStatus: TypeAlias = Literal[
    "Active",
    "Inactive",
    "RuntimeFailure",
    "ConnectionFailure",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Active",
        "Inactive",
        "RuntimeFailure",
        "ConnectionFailure",
    )
)


def to_query_text(value: PartnerIntegrationStatus) -> str:
    return value


def from_query_text(text: str) -> PartnerIntegrationStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown PartnerIntegrationStatus value: {text!r}")
    return cast(PartnerIntegrationStatus, text)


def serialize_query(
    value: PartnerIntegrationStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> PartnerIntegrationStatus:
    return from_query_text(el.text or "")
