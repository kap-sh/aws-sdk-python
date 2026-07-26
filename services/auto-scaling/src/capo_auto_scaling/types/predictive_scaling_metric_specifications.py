"""Generated from Smithy shape ``com.amazonaws.autoscaling#PredictiveScalingMetricSpecifications``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.predictive_scaling_metric_specification

PredictiveScalingMetricSpecifications: TypeAlias = list[
    "capo_auto_scaling.types.predictive_scaling_metric_specification.PredictiveScalingMetricSpecification"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: PredictiveScalingMetricSpecifications,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import capo_auto_scaling.types.predictive_scaling_metric_specification

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.predictive_scaling_metric_specification.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> PredictiveScalingMetricSpecifications:
    import capo_auto_scaling.types.predictive_scaling_metric_specification

    out: PredictiveScalingMetricSpecifications = []
    for child in el.findall("member"):
        out.append(
            capo_auto_scaling.types.predictive_scaling_metric_specification.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: PredictiveScalingMetricSpecifications,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    import capo_auto_scaling.types.predictive_scaling_metric_specification

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.predictive_scaling_metric_specification.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> PredictiveScalingMetricSpecifications:
    import capo_auto_scaling.types.predictive_scaling_metric_specification

    out: PredictiveScalingMetricSpecifications = []
    for child in parent.findall(tag):
        out.append(
            capo_auto_scaling.types.predictive_scaling_metric_specification.deserialize_query(
                child
            )
        )
    return out
