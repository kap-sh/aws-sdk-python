"""Generated from Smithy shape ``com.amazonaws.cloudwatch#AlarmType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch._protocol.xml import Element
from aws_sdk_cloudwatch.errors import DeserializationError

AlarmType: TypeAlias = Literal[
    "CompositeAlarm",
    "MetricAlarm",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CompositeAlarm",
        "MetricAlarm",
    )
)


def serialize_aws_json_1_0(value: AlarmType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AlarmType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AlarmType value: {data!r}")
    return cast(AlarmType, data)


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CompositeAlarm",
        "MetricAlarm",
    )
)


def to_query_text(value: AlarmType) -> str:
    return value


def from_query_text(text: str) -> AlarmType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown AlarmType value: {text!r}")
    return cast(AlarmType, text)


def serialize_query(
    value: AlarmType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AlarmType:
    return from_query_text(el.text or "")
