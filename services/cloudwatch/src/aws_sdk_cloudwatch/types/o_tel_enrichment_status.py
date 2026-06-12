"""Generated from Smithy shape ``com.amazonaws.cloudwatch#OTelEnrichmentStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch._protocol.xml import Element
from aws_sdk_cloudwatch.errors import DeserializationError

"""<p>The status of OTel enrichment for the account.</p>"""
OTelEnrichmentStatus: TypeAlias = Literal[
    "Running",
    "Stopped",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Running",
        "Stopped",
    )
)


def serialize_aws_json_1_0(value: OTelEnrichmentStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> OTelEnrichmentStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OTelEnrichmentStatus value: {data!r}")
    return cast(OTelEnrichmentStatus, data)


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Running",
        "Stopped",
    )
)


def to_query_text(value: OTelEnrichmentStatus) -> str:
    return value


def from_query_text(text: str) -> OTelEnrichmentStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown OTelEnrichmentStatus value: {text!r}")
    return cast(OTelEnrichmentStatus, text)


def serialize_query(
    value: OTelEnrichmentStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> OTelEnrichmentStatus:
    return from_query_text(el.text or "")
