"""Generated from Smithy shape ``com.amazonaws.cloudwatch#AnomalyDetectorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch._protocol.xml import Element
from aws_sdk_cloudwatch.errors import DeserializationError

AnomalyDetectorType: TypeAlias = Literal[
    "SINGLE_METRIC",
    "METRIC_MATH",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SINGLE_METRIC",
        "METRIC_MATH",
    )
)


def serialize_aws_json_1_0(value: AnomalyDetectorType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AnomalyDetectorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AnomalyDetectorType value: {data!r}")
    return cast(AnomalyDetectorType, data)


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SINGLE_METRIC",
        "METRIC_MATH",
    )
)


def to_query_text(value: AnomalyDetectorType) -> str:
    return value


def from_query_text(text: str) -> AnomalyDetectorType:
    if text not in _VALUES:
        raise DeserializationError(f"unknown AnomalyDetectorType value: {text!r}")
    return cast(AnomalyDetectorType, text)


def serialize_query(
    value: AnomalyDetectorType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> AnomalyDetectorType:
    return from_query_text(el.text or "")
