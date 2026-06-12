"""Generated from Smithy shape ``com.amazonaws.cloudwatch#AnomalyDetectorStateValue``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch._protocol.xml import Element
from aws_sdk_cloudwatch.errors import DeserializationError

AnomalyDetectorStateValue: TypeAlias = Literal[
    "PENDING_TRAINING",
    "TRAINED_INSUFFICIENT_DATA",
    "TRAINED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING_TRAINING",
        "TRAINED_INSUFFICIENT_DATA",
        "TRAINED",
    )
)


def serialize_aws_json_1_0(value: AnomalyDetectorStateValue) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AnomalyDetectorStateValue:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnomalyDetectorStateValue value: {data!r}")
    return cast(AnomalyDetectorStateValue, data)


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING_TRAINING",
        "TRAINED_INSUFFICIENT_DATA",
        "TRAINED",
    )
)


def to_query_text(value: AnomalyDetectorStateValue) -> str:
    return value


def from_query_text(text: str) -> AnomalyDetectorStateValue:
    if text not in _VALUES:
        raise DeserializationError(f"unknown AnomalyDetectorStateValue value: {text!r}")
    return cast(AnomalyDetectorStateValue, text)


def serialize_query(
    value: AnomalyDetectorStateValue, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AnomalyDetectorStateValue:
    return from_query_text(el.text or "")
