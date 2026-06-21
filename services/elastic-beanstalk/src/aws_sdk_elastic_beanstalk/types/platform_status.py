"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#PlatformStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_beanstalk._protocol.xml import Element

PlatformStatus: TypeAlias = Literal[
    "Creating",
    "Failed",
    "Ready",
    "Deleting",
    "Deleted",
]


# --- awsQuery ser/de ---
def to_query_text(value: PlatformStatus) -> str:
    return value


def from_query_text(text: str) -> PlatformStatus:
    return cast(PlatformStatus, text)


def serialize_query(
    value: PlatformStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> PlatformStatus:
    return from_query_text(el.text or "")
