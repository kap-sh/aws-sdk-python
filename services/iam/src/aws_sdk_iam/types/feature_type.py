"""Generated from Smithy shape ``com.amazonaws.iam#FeatureType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iam._protocol.xml import Element

FeatureType: TypeAlias = Literal[
    "RootCredentialsManagement",
    "RootSessions",
]


# --- awsQuery ser/de ---
def to_query_text(value: FeatureType) -> str:
    return value


def from_query_text(text: str) -> FeatureType:
    return cast(FeatureType, text)


def serialize_query(
    value: FeatureType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> FeatureType:
    return from_query_text(el.text or "")
