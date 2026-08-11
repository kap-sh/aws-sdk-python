"""Generated from Smithy shape ``com.amazonaws.ec2#CreateFleetErrorsSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.create_fleet_error

CreateFleetErrorsSet: TypeAlias = list[
    "capo_ec2.types.create_fleet_error.CreateFleetError"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateFleetErrorsSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.create_fleet_error

        capo_ec2.types.create_fleet_error.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> CreateFleetErrorsSet:
    import capo_ec2.types.create_fleet_error

    out: CreateFleetErrorsSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.create_fleet_error.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> CreateFleetErrorsSet:
    import capo_ec2.types.create_fleet_error

    out: CreateFleetErrorsSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.create_fleet_error.deserialize_ec2_query(child))
    return out
