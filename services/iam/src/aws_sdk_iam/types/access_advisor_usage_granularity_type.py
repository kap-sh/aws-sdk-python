"""Generated from Smithy shape ``com.amazonaws.iam#AccessAdvisorUsageGranularityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iam._protocol.xml import Element

AccessAdvisorUsageGranularityType: TypeAlias = Literal[
    "SERVICE_LEVEL",
    "ACTION_LEVEL",
]


# --- awsQuery ser/de ---
def to_query_text(value: AccessAdvisorUsageGranularityType) -> str:
    return value


def from_query_text(text: str) -> AccessAdvisorUsageGranularityType:
    return cast(AccessAdvisorUsageGranularityType, text)


def serialize_query(
    value: AccessAdvisorUsageGranularityType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AccessAdvisorUsageGranularityType:
    return from_query_text(el.text or "")
