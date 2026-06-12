"""Generated from Smithy shape ``com.amazonaws.autoscaling#PredictiveScalingMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling._protocol.xml import Element
from aws_sdk_auto_scaling.errors import DeserializationError

PredictiveScalingMode: TypeAlias = Literal[
    "ForecastAndScale",
    "ForecastOnly",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ForecastAndScale",
        "ForecastOnly",
    )
)


def to_query_text(value: PredictiveScalingMode) -> str:
    return value


def from_query_text(text: str) -> PredictiveScalingMode:
    if text not in _VALUES:
        raise DeserializationError(f"unknown PredictiveScalingMode value: {text!r}")
    return cast(PredictiveScalingMode, text)


def serialize_query(
    value: PredictiveScalingMode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> PredictiveScalingMode:
    return from_query_text(el.text or "")
