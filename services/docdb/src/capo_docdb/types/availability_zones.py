"""Generated from Smithy shape ``com.amazonaws.docdb#AvailabilityZones``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_docdb._protocol.xml import Element

if TYPE_CHECKING:
    import capo_docdb.types.string

AvailabilityZones: TypeAlias = list["capo_docdb.types.string.String"]


# --- awsQuery ser/de ---
def serialize_query(
    value: AvailabilityZones, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.AvailabilityZone.{n}", str(item)))


def deserialize_query(el: Element) -> AvailabilityZones:
    out: AvailabilityZones = []
    for child in el.findall("AvailabilityZone"):
        out.append(str(child.text or ""))
    return out


def serialize_query_flat(
    value: AvailabilityZones, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        pairs.append((f"{prefix}.{n}", str(item)))


def deserialize_query_flat(parent: Element, tag: str) -> AvailabilityZones:
    out: AvailabilityZones = []
    for child in parent.findall(tag):
        out.append(str(child.text or ""))
    return out
