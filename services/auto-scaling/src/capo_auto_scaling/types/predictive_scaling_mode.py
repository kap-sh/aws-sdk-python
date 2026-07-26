"""Generated from Smithy shape ``com.amazonaws.autoscaling#PredictiveScalingMode``."""

from typing import Literal, TypeAlias, cast

from capo_auto_scaling._protocol.xml import Element

PredictiveScalingMode: TypeAlias = Literal[
    "ForecastAndScale",
    "ForecastOnly",
]


# --- awsQuery ser/de ---
def to_query_text(value: PredictiveScalingMode) -> str:
    return value


def from_query_text(text: str) -> PredictiveScalingMode:
    return cast(PredictiveScalingMode, text)


def serialize_query(
    value: PredictiveScalingMode, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> PredictiveScalingMode:
    return from_query_text(el.text or "")
