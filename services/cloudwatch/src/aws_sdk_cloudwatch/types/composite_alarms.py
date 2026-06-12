"""Generated from Smithy shape ``com.amazonaws.cloudwatch#CompositeAlarms``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_cloudwatch.types.composite_alarm

CompositeAlarms: TypeAlias = list[
    "aws_sdk_cloudwatch.types.composite_alarm.CompositeAlarm"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: CompositeAlarms, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudwatch.types.composite_alarm

    for n, item in enumerate(value, 1):
        aws_sdk_cloudwatch.types.composite_alarm.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> CompositeAlarms:
    import aws_sdk_cloudwatch.types.composite_alarm

    out: CompositeAlarms = []
    for child in el.findall("member"):
        out.append(aws_sdk_cloudwatch.types.composite_alarm.deserialize_query(child))
    return out


def serialize_query_flat(
    value: CompositeAlarms, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_cloudwatch.types.composite_alarm

    for n, item in enumerate(value, 1):
        aws_sdk_cloudwatch.types.composite_alarm.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> CompositeAlarms:
    import aws_sdk_cloudwatch.types.composite_alarm

    out: CompositeAlarms = []
    for child in parent.findall(tag):
        out.append(aws_sdk_cloudwatch.types.composite_alarm.deserialize_query(child))
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CompositeAlarms) -> list:
    import aws_sdk_cloudwatch.types.composite_alarm

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudwatch.types.composite_alarm.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> CompositeAlarms:
    import aws_sdk_cloudwatch.types.composite_alarm

    out: CompositeAlarms = []
    for item in data:
        out.append(
            aws_sdk_cloudwatch.types.composite_alarm.deserialize_aws_json_1_0(item)
        )
    return out
