"""Generated from Smithy shape ``com.amazonaws.ec2#AcceleratorManufacturerSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.accelerator_manufacturer

AcceleratorManufacturerSet: TypeAlias = list[
    "capo_ec2.types.accelerator_manufacturer.AcceleratorManufacturer"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AcceleratorManufacturerSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.accelerator_manufacturer

        capo_ec2.types.accelerator_manufacturer.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> AcceleratorManufacturerSet:
    import capo_ec2.types.accelerator_manufacturer

    out: AcceleratorManufacturerSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.accelerator_manufacturer.deserialize_ec2_query(child))
    return out
