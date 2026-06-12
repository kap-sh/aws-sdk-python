"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ComputeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_beanstalk._protocol.xml import Element
from aws_sdk_elastic_beanstalk.errors import DeserializationError

ComputeType: TypeAlias = Literal[
    "BUILD_GENERAL1_SMALL",
    "BUILD_GENERAL1_MEDIUM",
    "BUILD_GENERAL1_LARGE",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "BUILD_GENERAL1_SMALL",
        "BUILD_GENERAL1_MEDIUM",
        "BUILD_GENERAL1_LARGE",
    )
)


def to_query_text(value: ComputeType) -> str:
    return value


def from_query_text(text: str) -> ComputeType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown ComputeType value: {text!r}")
    return cast(ComputeType, text)


def serialize_query(
    value: ComputeType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> ComputeType:
    return from_query_text(el.text or "")
