"""Generated from Smithy shape ``com.amazonaws.cloudwatch#MetricDataResultMessages``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.message_data

MetricDataResultMessages: TypeAlias = list[
    "aws_sdk_cloudwatch.types.message_data.MessageData"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: MetricDataResultMessages, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudwatch.types.message_data

    for n, item in enumerate(value, 1):
        aws_sdk_cloudwatch.types.message_data.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> MetricDataResultMessages:
    import aws_sdk_cloudwatch.types.message_data

    out: MetricDataResultMessages = []
    for child in el.findall("member"):
        out.append(aws_sdk_cloudwatch.types.message_data.deserialize_query(child))
    return out


def serialize_query_flat(
    value: MetricDataResultMessages, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudwatch.types.message_data

    for n, item in enumerate(value, 1):
        aws_sdk_cloudwatch.types.message_data.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> MetricDataResultMessages:
    import aws_sdk_cloudwatch.types.message_data

    out: MetricDataResultMessages = []
    for child in parent.findall(tag):
        out.append(aws_sdk_cloudwatch.types.message_data.deserialize_query(child))
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MetricDataResultMessages) -> list:
    import aws_sdk_cloudwatch.types.message_data

    out: list = []
    for item in value:
        out.append(aws_sdk_cloudwatch.types.message_data.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> MetricDataResultMessages:
    import aws_sdk_cloudwatch.types.message_data

    out: MetricDataResultMessages = []
    for item in data:
        out.append(aws_sdk_cloudwatch.types.message_data.deserialize_aws_json_1_0(item))
    return out
