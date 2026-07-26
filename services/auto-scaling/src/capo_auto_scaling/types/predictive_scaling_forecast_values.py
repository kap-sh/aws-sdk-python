"""Generated from Smithy shape ``com.amazonaws.autoscaling#PredictiveScalingForecastValues``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.metric_scale

PredictiveScalingForecastValues: TypeAlias = list[
    "capo_auto_scaling.types.metric_scale.MetricScale"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: PredictiveScalingForecastValues, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> PredictiveScalingForecastValues:
    out: PredictiveScalingForecastValues = []
    for child in el.findall("member"):
        out.append(float(child.text or ""))
    return out


def serialize_query_flat(
    value: PredictiveScalingForecastValues, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(
    parent: Element, tag: str
) -> PredictiveScalingForecastValues:
    out: PredictiveScalingForecastValues = []
    for child in parent.findall(tag):
        out.append(float(child.text or ""))
    return out
