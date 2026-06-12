"""Generated from Smithy shape ``com.amazonaws.autoscaling#TargetTrackingMetricDataQueries``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.target_tracking_metric_data_query

TargetTrackingMetricDataQueries: TypeAlias = list[
    "aws_sdk_auto_scaling.types.target_tracking_metric_data_query.TargetTrackingMetricDataQuery"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: TargetTrackingMetricDataQueries, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_auto_scaling.types.target_tracking_metric_data_query

    for n, item in enumerate(value, 1):
        aws_sdk_auto_scaling.types.target_tracking_metric_data_query.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> TargetTrackingMetricDataQueries:
    import aws_sdk_auto_scaling.types.target_tracking_metric_data_query

    out: TargetTrackingMetricDataQueries = []
    for child in el.findall("member"):
        out.append(
            aws_sdk_auto_scaling.types.target_tracking_metric_data_query.deserialize_query(
                child
            )
        )
    return out


def serialize_query_flat(
    value: TargetTrackingMetricDataQueries, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_auto_scaling.types.target_tracking_metric_data_query

    for n, item in enumerate(value, 1):
        aws_sdk_auto_scaling.types.target_tracking_metric_data_query.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(
    parent: Element, tag: str
) -> TargetTrackingMetricDataQueries:
    import aws_sdk_auto_scaling.types.target_tracking_metric_data_query

    out: TargetTrackingMetricDataQueries = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_auto_scaling.types.target_tracking_metric_data_query.deserialize_query(
                child
            )
        )
    return out
