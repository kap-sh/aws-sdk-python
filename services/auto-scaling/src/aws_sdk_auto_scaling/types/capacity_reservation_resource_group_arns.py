"""Generated from Smithy shape ``com.amazonaws.autoscaling#CapacityReservationResourceGroupArns``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.resource_name

CapacityReservationResourceGroupArns: TypeAlias = list[
    "aws_sdk_auto_scaling.types.resource_name.ResourceName"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: CapacityReservationResourceGroupArns,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.member.{n}", str(item)))


def deserialize_query(el: Element) -> CapacityReservationResourceGroupArns:
    out: CapacityReservationResourceGroupArns = []
    for child in el.findall("member"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: CapacityReservationResourceGroupArns,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(
    parent: Element, tag: str
) -> CapacityReservationResourceGroupArns:
    out: CapacityReservationResourceGroupArns = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
