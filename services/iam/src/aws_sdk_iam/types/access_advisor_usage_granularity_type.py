"""Generated from Smithy shape ``com.amazonaws.iam#AccessAdvisorUsageGranularityType``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_iam.errors import DeserializationError
from aws_sdk_iam._protocol.xml import Element

AccessAdvisorUsageGranularityType: TypeAlias = Literal[
    "SERVICE_LEVEL",
    "ACTION_LEVEL",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SERVICE_LEVEL",
        "ACTION_LEVEL",
    )
)


def to_query_text(value: AccessAdvisorUsageGranularityType) -> str:
    return value


def from_query_text(text: str) -> AccessAdvisorUsageGranularityType:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown AccessAdvisorUsageGranularityType value: {text!r}"
        )
    return cast(AccessAdvisorUsageGranularityType, text)


def serialize_query(
    value: AccessAdvisorUsageGranularityType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AccessAdvisorUsageGranularityType:
    return from_query_text(el.text or "")
