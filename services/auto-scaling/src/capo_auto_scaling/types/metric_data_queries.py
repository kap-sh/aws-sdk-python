"""Generated from Smithy shape ``com.amazonaws.autoscaling#MetricDataQueries``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.metric_data_query

MetricDataQueries: TypeAlias = list[
    "capo_auto_scaling.types.metric_data_query.MetricDataQuery"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: MetricDataQueries, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.metric_data_query

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.metric_data_query.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> MetricDataQueries:
    import capo_auto_scaling.types.metric_data_query

    out: MetricDataQueries = []
    for child in el.findall("member"):
        out.append(capo_auto_scaling.types.metric_data_query.deserialize_query(child))
    return out


def serialize_query_flat(
    value: MetricDataQueries, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.metric_data_query

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.metric_data_query.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> MetricDataQueries:
    import capo_auto_scaling.types.metric_data_query

    out: MetricDataQueries = []
    for child in parent.findall(tag):
        out.append(capo_auto_scaling.types.metric_data_query.deserialize_query(child))
    return out
