"""Generated from Smithy shape ``com.amazonaws.redshift#ScheduledActionTimeList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_redshift._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_redshift.types.t_stamp

ScheduledActionTimeList: TypeAlias = list["aws_sdk_redshift.types.t_stamp.TStamp"]


# --- awsQuery ser/de ---
def serialize_query(
    value: ScheduledActionTimeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.t_stamp

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.t_stamp.serialize_query(
            item, pairs, f"{prefix}.ScheduledActionTime.{n}"
        )


def deserialize_query(el: Element) -> ScheduledActionTimeList:
    import aws_sdk_redshift.types.t_stamp

    out: ScheduledActionTimeList = []
    for child in el.findall("ScheduledActionTime"):
        out.append(aws_sdk_redshift.types.t_stamp.deserialize_query(child))
    return out


def serialize_query_flat(
    value: ScheduledActionTimeList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_redshift.types.t_stamp

    for n, item in enumerate(value, 1):
        aws_sdk_redshift.types.t_stamp.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> ScheduledActionTimeList:
    import aws_sdk_redshift.types.t_stamp

    out: ScheduledActionTimeList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_redshift.types.t_stamp.deserialize_query(child))
    return out
