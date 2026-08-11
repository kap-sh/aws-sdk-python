"""Generated from Smithy shape ``com.amazonaws.rds#AvailabilityZoneList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.availability_zone

AvailabilityZoneList: TypeAlias = list[
    "capo_rds.types.availability_zone.AvailabilityZone"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: AvailabilityZoneList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.availability_zone

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.availability_zone.serialize_query(
            item, pairs, f"{prefix}.AvailabilityZone.{n}"
        )


def deserialize_query(el: Element) -> AvailabilityZoneList:
    import capo_rds.types.availability_zone

    out: AvailabilityZoneList = []
    for child in el.findall("AvailabilityZone"):
        out.append(capo_rds.types.availability_zone.deserialize_query(child))
    return out


def serialize_query_flat(
    value: AvailabilityZoneList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.availability_zone

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.availability_zone.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> AvailabilityZoneList:
    import capo_rds.types.availability_zone

    out: AvailabilityZoneList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.availability_zone.deserialize_query(child))
    return out
