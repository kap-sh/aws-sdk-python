"""Generated from Smithy shape ``com.amazonaws.cloudformation#OrganizationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudformation._protocol.xml import Element

OrganizationStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "DISABLED_PERMANENTLY",
]


# --- awsQuery ser/de ---
def to_query_text(value: OrganizationStatus) -> str:
    return value


def from_query_text(text: str) -> OrganizationStatus:
    return cast(OrganizationStatus, text)


def serialize_query(
    value: OrganizationStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> OrganizationStatus:
    return from_query_text(el.text or "")
