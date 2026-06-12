"""Generated from Smithy shape ``com.amazonaws.cloudwatch#EntityMetricDataList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.entity_metric_data

EntityMetricDataList: TypeAlias = list[
    "aws_sdk_cloudwatch.types.entity_metric_data.EntityMetricData"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: EntityMetricDataList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudwatch.types.entity_metric_data

    for n, item in enumerate(value, 1):
        aws_sdk_cloudwatch.types.entity_metric_data.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> EntityMetricDataList:
    import aws_sdk_cloudwatch.types.entity_metric_data

    out: EntityMetricDataList = []
    for child in el.findall("member"):
        out.append(aws_sdk_cloudwatch.types.entity_metric_data.deserialize_query(child))
    return out


def serialize_query_flat(
    value: EntityMetricDataList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudwatch.types.entity_metric_data

    for n, item in enumerate(value, 1):
        aws_sdk_cloudwatch.types.entity_metric_data.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> EntityMetricDataList:
    import aws_sdk_cloudwatch.types.entity_metric_data

    out: EntityMetricDataList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_cloudwatch.types.entity_metric_data.deserialize_query(child))
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EntityMetricDataList) -> list:
    import aws_sdk_cloudwatch.types.entity_metric_data

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch.types.entity_metric_data.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EntityMetricDataList:
    import aws_sdk_cloudwatch.types.entity_metric_data

    out: EntityMetricDataList = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch.types.entity_metric_data.deserialize_aws_json_1_0(item)
        )
    return out
