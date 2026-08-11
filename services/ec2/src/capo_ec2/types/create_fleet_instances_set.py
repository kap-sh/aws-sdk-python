"""Generated from Smithy shape ``com.amazonaws.ec2#CreateFleetInstancesSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.create_fleet_instance

CreateFleetInstancesSet: TypeAlias = list[
    "capo_ec2.types.create_fleet_instance.CreateFleetInstance"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateFleetInstancesSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.create_fleet_instance

        capo_ec2.types.create_fleet_instance.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> CreateFleetInstancesSet:
    import capo_ec2.types.create_fleet_instance

    out: CreateFleetInstancesSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.create_fleet_instance.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> CreateFleetInstancesSet:
    import capo_ec2.types.create_fleet_instance

    out: CreateFleetInstancesSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.create_fleet_instance.deserialize_ec2_query(child))
    return out
