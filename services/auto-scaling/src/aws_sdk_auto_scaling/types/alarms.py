"""Generated from Smithy shape ``com.amazonaws.autoscaling#Alarms``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.alarm

Alarms: TypeAlias = list["aws_sdk_auto_scaling.types.alarm.Alarm"]


# --- awsQuery ser/de ---
def serialize_query(value: Alarms, pairs: list[tuple[str, str]], prefix: str) -> None:
    import aws_sdk_auto_scaling.types.alarm

    for n, item in enumerate(value, 1):
        aws_sdk_auto_scaling.types.alarm.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> Alarms:
    import aws_sdk_auto_scaling.types.alarm

    out: Alarms = []
    for child in el.findall("member"):
        out.append(aws_sdk_auto_scaling.types.alarm.deserialize_query(child))
    return out


def serialize_query_flat(
    value: Alarms, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_auto_scaling.types.alarm

    for n, item in enumerate(value, 1):
        aws_sdk_auto_scaling.types.alarm.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> Alarms:
    import aws_sdk_auto_scaling.types.alarm

    out: Alarms = []
    for child in parent.findall(tag):
        out.append(aws_sdk_auto_scaling.types.alarm.deserialize_query(child))
    return out
