"""Generated from Smithy shape ``com.amazonaws.cloudwatch#Statistic``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch._protocol.xml import Element
from aws_sdk_cloudwatch.errors import DeserializationError

Statistic: TypeAlias = Literal[
    "SampleCount",
    "Average",
    "Sum",
    "Minimum",
    "Maximum",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SampleCount",
        "Average",
        "Sum",
        "Minimum",
        "Maximum",
    )
)


def serialize_aws_json_1_0(value: Statistic) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Statistic:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Statistic value: {data!r}")
    return cast(Statistic, data)


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SampleCount",
        "Average",
        "Sum",
        "Minimum",
        "Maximum",
    )
)


def to_query_text(value: Statistic) -> str:
    return value


def from_query_text(text: str) -> Statistic:
    if text not in _VALUES:
        raise DeserializationError(f"unknown Statistic value: {text!r}")
    return cast(Statistic, text)


def serialize_query(
    value: Statistic, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> Statistic:
    return from_query_text(el.text or "")
