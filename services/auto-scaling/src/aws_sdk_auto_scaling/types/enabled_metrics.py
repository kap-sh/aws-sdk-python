"""Generated from Smithy shape ``com.amazonaws.autoscaling#EnabledMetrics``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.enabled_metric

EnabledMetrics: TypeAlias = list[
    "aws_sdk_auto_scaling.types.enabled_metric.EnabledMetric"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: EnabledMetrics, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_auto_scaling.types.enabled_metric

    for n, item in enumerate(value, 1):
        aws_sdk_auto_scaling.types.enabled_metric.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> EnabledMetrics:
    import aws_sdk_auto_scaling.types.enabled_metric

    out: EnabledMetrics = []
    for child in el.findall("member"):
        out.append(aws_sdk_auto_scaling.types.enabled_metric.deserialize_query(child))
    return out


def serialize_query_flat(
    value: EnabledMetrics, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_auto_scaling.types.enabled_metric

    for n, item in enumerate(value, 1):
        aws_sdk_auto_scaling.types.enabled_metric.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> EnabledMetrics:
    import aws_sdk_auto_scaling.types.enabled_metric

    out: EnabledMetrics = []
    for child in parent.findall(tag):
        out.append(aws_sdk_auto_scaling.types.enabled_metric.deserialize_query(child))
    return out
