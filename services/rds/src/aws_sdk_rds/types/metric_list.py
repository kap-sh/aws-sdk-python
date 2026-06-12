"""Generated from Smithy shape ``com.amazonaws.rds#MetricList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.metric

MetricList: TypeAlias = list["aws_sdk_rds.types.metric.Metric"]


# --- awsQuery ser/de ---
def serialize_query(
    value: MetricList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.metric

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.metric.serialize_query(item, pairs, f"{prefix}.member.{n}")


def deserialize_query(el: Element) -> MetricList:
    import aws_sdk_rds.types.metric

    out: MetricList = []
    for child in el.findall("member"):
        out.append(aws_sdk_rds.types.metric.deserialize_query(child))
    return out


def serialize_query_flat(
    value: MetricList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_rds.types.metric

    for n, item in enumerate(value, 1):
        aws_sdk_rds.types.metric.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> MetricList:
    import aws_sdk_rds.types.metric

    out: MetricList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_rds.types.metric.deserialize_query(child))
    return out
