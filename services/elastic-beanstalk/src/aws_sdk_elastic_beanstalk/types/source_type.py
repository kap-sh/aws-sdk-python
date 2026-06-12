"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#SourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_beanstalk._protocol.xml import Element
from aws_sdk_elastic_beanstalk.errors import DeserializationError

SourceType: TypeAlias = Literal[
    "Git",
    "Zip",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Git",
        "Zip",
    )
)


def to_query_text(value: SourceType) -> str:
    return value


def from_query_text(text: str) -> SourceType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown SourceType value: {text!r}")
    return cast(SourceType, text)


def serialize_query(
    value: SourceType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> SourceType:
    return from_query_text(el.text or "")
