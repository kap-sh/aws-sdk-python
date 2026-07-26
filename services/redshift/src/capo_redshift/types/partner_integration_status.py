"""Generated from Smithy shape ``com.amazonaws.redshift#PartnerIntegrationStatus``."""

from typing import Literal, TypeAlias, cast

from capo_redshift._protocol.xml import Element

PartnerIntegrationStatus: TypeAlias = Literal[
    "Active",
    "Inactive",
    "RuntimeFailure",
    "ConnectionFailure",
]


# --- awsQuery ser/de ---
def to_query_text(value: PartnerIntegrationStatus) -> str:
    return value


def from_query_text(text: str) -> PartnerIntegrationStatus:
    return cast(PartnerIntegrationStatus, text)


def serialize_query(
    value: PartnerIntegrationStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> PartnerIntegrationStatus:
    return from_query_text(el.text or "")
