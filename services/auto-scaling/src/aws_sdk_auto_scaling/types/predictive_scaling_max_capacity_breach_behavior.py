"""Generated from Smithy shape ``com.amazonaws.autoscaling#PredictiveScalingMaxCapacityBreachBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_auto_scaling._protocol.xml import Element
from aws_sdk_auto_scaling.errors import DeserializationError

PredictiveScalingMaxCapacityBreachBehavior: TypeAlias = Literal[
    "HonorMaxCapacity",
    "IncreaseMaxCapacity",
]


# --- awsQuery ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HonorMaxCapacity",
        "IncreaseMaxCapacity",
    )
)


def to_query_text(value: PredictiveScalingMaxCapacityBreachBehavior) -> str:
    return value


def from_query_text(text: str) -> PredictiveScalingMaxCapacityBreachBehavior:
    if text not in _VALUES:
        raise DeserializationError(
            f"unknown PredictiveScalingMaxCapacityBreachBehavior value: {text!r}"
        )
    return cast(PredictiveScalingMaxCapacityBreachBehavior, text)


def serialize_query(
    value: PredictiveScalingMaxCapacityBreachBehavior,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> PredictiveScalingMaxCapacityBreachBehavior:
    return from_query_text(el.text or "")
