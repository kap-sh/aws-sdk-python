"""Generated from Smithy shape ``com.amazonaws.ec2#FleetSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.fleet_data

FleetSet: TypeAlias = list["capo_ec2.types.fleet_data.FleetData"]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FleetSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.fleet_data

        capo_ec2.types.fleet_data.serialize_ec2_query(item, pairs, f"{prefix}.{n}")


def deserialize_ec2_query(el: Element) -> FleetSet:
    import capo_ec2.types.fleet_data

    out: FleetSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.fleet_data.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> FleetSet:
    import capo_ec2.types.fleet_data

    out: FleetSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.fleet_data.deserialize_ec2_query(child))
    return out
