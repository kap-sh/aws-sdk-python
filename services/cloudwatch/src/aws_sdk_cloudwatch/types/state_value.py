"""Generated from Smithy shape ``com.amazonaws.cloudwatch#StateValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch._protocol.xml import Element
from aws_sdk_cloudwatch.errors import DeserializationError

StateValue: TypeAlias = Literal[
    "OK",
    "ALARM",
    "INSUFFICIENT_DATA",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OK",
        "ALARM",
        "INSUFFICIENT_DATA",
    )
)


def serialize_aws_json_1_0(value: StateValue) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StateValue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StateValue value: {data!r}")
    return cast(StateValue, data)


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OK",
        "ALARM",
        "INSUFFICIENT_DATA",
    )
)


def to_query_text(value: StateValue) -> str:
    return value


def from_query_text(text: str) -> StateValue:
    if text not in _VALUES:
        raise DeserializationError(f"unknown StateValue value: {text!r}")
    return cast(StateValue, text)


def serialize_query(
    value: StateValue, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> StateValue:
    return from_query_text(el.text or "")
