"""Generated from Smithy shape ``com.amazonaws.neptune#AvailabilityZoneList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_neptune._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_neptune.types.availability_zone

AvailabilityZoneList: TypeAlias = list[
    "aws_sdk_neptune.types.availability_zone.AvailabilityZone"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: AvailabilityZoneList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_neptune.types.availability_zone

    for n, item in enumerate(value, 1):
        aws_sdk_neptune.types.availability_zone.serialize_query(
            item, pairs, f"{prefix}.AvailabilityZone.{n}"
        )


def deserialize_query(el: Element) -> AvailabilityZoneList:
    import aws_sdk_neptune.types.availability_zone

    out: AvailabilityZoneList = []
    for child in el.findall("AvailabilityZone"):
        out.append(aws_sdk_neptune.types.availability_zone.deserialize_query(child))
    return out


def serialize_query_flat(
    value: AvailabilityZoneList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import aws_sdk_neptune.types.availability_zone

    for n, item in enumerate(value, 1):
        aws_sdk_neptune.types.availability_zone.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> AvailabilityZoneList:
    import aws_sdk_neptune.types.availability_zone

    out: AvailabilityZoneList = []
    for child in parent.findall(tag):
        out.append(aws_sdk_neptune.types.availability_zone.deserialize_query(child))
    return out
