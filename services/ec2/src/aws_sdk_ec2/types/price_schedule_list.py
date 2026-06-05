"""Generated from Smithy shape ``com.amazonaws.ec2#PriceScheduleList``."""

from typing import TYPE_CHECKING, TypeAlias
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.price_schedule

PriceScheduleList: TypeAlias = list["aws_sdk_ec2.types.price_schedule.PriceSchedule"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PriceScheduleList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.price_schedule

        aws_sdk_ec2.types.price_schedule.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> PriceScheduleList:
    import aws_sdk_ec2.types.price_schedule

    out: PriceScheduleList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_ec2.types.price_schedule.deserialize_ec2_query(child))
    return out
