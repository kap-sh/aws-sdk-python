"""Generated from Smithy shape ``com.amazonaws.rds#ClusterScalabilityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_rds._protocol.xml import Element

ClusterScalabilityType: TypeAlias = Literal[
    "standard",
    "limitless",
]


# --- awsQuery ser/de ---
def to_query_text(value: ClusterScalabilityType) -> str:
    return value


def from_query_text(text: str) -> ClusterScalabilityType:
    return cast(ClusterScalabilityType, text)


def serialize_query(
    value: ClusterScalabilityType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ClusterScalabilityType:
    return from_query_text(el.text or "")
