"""Generated from Smithy shape ``com.amazonaws.ec2#PriceScheduleSpecificationList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.price_schedule_specification

PriceScheduleSpecificationList: TypeAlias = list[
    "aws_sdk_ec2.types.price_schedule_specification.PriceScheduleSpecification"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PriceScheduleSpecificationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.price_schedule_specification

        aws_sdk_ec2.types.price_schedule_specification.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> PriceScheduleSpecificationList:
    import aws_sdk_ec2.types.price_schedule_specification

    out: PriceScheduleSpecificationList = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.price_schedule_specification.deserialize_ec2_query(child)
        )
    return out
