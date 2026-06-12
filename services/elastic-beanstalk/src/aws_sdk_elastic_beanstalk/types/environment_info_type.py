"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#EnvironmentInfoType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_beanstalk._protocol.xml import Element
from aws_sdk_elastic_beanstalk.errors import DeserializationError

EnvironmentInfoType: TypeAlias = Literal[
    "tail",
    "bundle",
    "analyze",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "tail",
        "bundle",
        "analyze",
    )
)


def to_query_text(value: EnvironmentInfoType) -> str:
    return value


def from_query_text(text: str) -> EnvironmentInfoType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown EnvironmentInfoType value: {text!r}")
    return cast(EnvironmentInfoType, text)


def serialize_query(
    value: EnvironmentInfoType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> EnvironmentInfoType:
    return from_query_text(el.text or "")
