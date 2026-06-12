"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#PlatformStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_beanstalk._protocol.xml import Element
from aws_sdk_elastic_beanstalk.errors import DeserializationError

PlatformStatus: TypeAlias = Literal[
    "Creating",
    "Failed",
    "Ready",
    "Deleting",
    "Deleted",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Creating",
        "Failed",
        "Ready",
        "Deleting",
        "Deleted",
    )
)


def to_query_text(value: PlatformStatus) -> str:
    return value


def from_query_text(text: str) -> PlatformStatus:
    if text not in _VALUES:
        raise DeserializationError(f"unknown PlatformStatus value: {text!r}")
    return cast(PlatformStatus, text)


def serialize_query(
    value: PlatformStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> PlatformStatus:
    return from_query_text(el.text or "")
