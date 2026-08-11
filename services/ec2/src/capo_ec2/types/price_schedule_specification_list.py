"""Generated from Smithy shape ``com.amazonaws.ec2#PriceScheduleSpecificationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.price_schedule_specification

PriceScheduleSpecificationList: TypeAlias = list[
    "capo_ec2.types.price_schedule_specification.PriceScheduleSpecification"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PriceScheduleSpecificationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.price_schedule_specification

        capo_ec2.types.price_schedule_specification.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> PriceScheduleSpecificationList:
    import capo_ec2.types.price_schedule_specification

    out: PriceScheduleSpecificationList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.price_schedule_specification.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> PriceScheduleSpecificationList:
    import capo_ec2.types.price_schedule_specification

    out: PriceScheduleSpecificationList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.price_schedule_specification.deserialize_ec2_query(child)
        )
    return out
