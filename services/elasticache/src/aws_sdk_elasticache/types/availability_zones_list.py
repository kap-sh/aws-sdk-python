"""Generated from Smithy shape ``com.amazonaws.elasticache#AvailabilityZonesList``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.string

AvailabilityZonesList: TypeAlias = list["aws_sdk_elasticache.types.string.String"]


# --- awsQuery ser/de ---
def serialize_query(
    value: AvailabilityZonesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.AvailabilityZone.{n}", str(item)))


def deserialize_query(el: Element) -> AvailabilityZonesList:
    out: AvailabilityZonesList = []
    for child in el.findall("AvailabilityZone"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: AvailabilityZonesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> AvailabilityZonesList:
    out: AvailabilityZonesList = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
