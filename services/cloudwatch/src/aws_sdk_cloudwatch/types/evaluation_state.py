"""Generated from Smithy shape ``com.amazonaws.cloudwatch#EvaluationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudwatch._protocol.xml import Element
from aws_sdk_cloudwatch.errors import DeserializationError

EvaluationState: TypeAlias = Literal[
    "PARTIAL_DATA",
    "EVALUATION_FAILURE",
    "EVALUATION_ERROR",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PARTIAL_DATA",
        "EVALUATION_FAILURE",
        "EVALUATION_ERROR",
    )
)


def serialize_aws_json_1_0(value: EvaluationState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EvaluationState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EvaluationState value: {data!r}")
    return cast(EvaluationState, data)


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PARTIAL_DATA",
        "EVALUATION_FAILURE",
        "EVALUATION_ERROR",
    )
)


def to_query_text(value: EvaluationState) -> str:
    return value


def from_query_text(text: str) -> EvaluationState:
    if text not in _VALUES:
        raise DeserializationError(f"unknown EvaluationState value: {text!r}")
    return cast(EvaluationState, text)


def serialize_query(
    value: EvaluationState, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> EvaluationState:
    return from_query_text(el.text or "")
