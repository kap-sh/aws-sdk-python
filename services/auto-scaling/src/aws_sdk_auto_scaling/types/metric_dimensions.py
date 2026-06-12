"""Generated from Smithy shape ``com.amazonaws.autoscaling#MetricDimensions``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.metric_dimension

MetricDimensions: TypeAlias = list[
    "aws_sdk_auto_scaling.types.metric_dimension.MetricDimension"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: MetricDimensions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_auto_scaling.types.metric_dimension

    for n, item in enumerate(value, 1):
        aws_sdk_auto_scaling.types.metric_dimension.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> MetricDimensions:
    import aws_sdk_auto_scaling.types.metric_dimension

    out: MetricDimensions = []
    for child in el.findall("member"):
        out.append(aws_sdk_auto_scaling.types.metric_dimension.deserialize_query(child))
    return out


def serialize_query_flat(
    value: MetricDimensions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_auto_scaling.types.metric_dimension

    for n, item in enumerate(value, 1):
        aws_sdk_auto_scaling.types.metric_dimension.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> MetricDimensions:
    import aws_sdk_auto_scaling.types.metric_dimension

    out: MetricDimensions = []
    for child in parent.findall(tag):
        out.append(aws_sdk_auto_scaling.types.metric_dimension.deserialize_query(child))
    return out
