"""Generated from Smithy shape ``com.amazonaws.autoscaling#AcceleratorManufacturers``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.accelerator_manufacturer

AcceleratorManufacturers: TypeAlias = list[
    "capo_auto_scaling.types.accelerator_manufacturer.AcceleratorManufacturer"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: AcceleratorManufacturers, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.accelerator_manufacturer

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.accelerator_manufacturer.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> AcceleratorManufacturers:
    import capo_auto_scaling.types.accelerator_manufacturer

    out: AcceleratorManufacturers = []
    for child in el.findall("member"):
        out.append(
            capo_auto_scaling.types.accelerator_manufacturer.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: AcceleratorManufacturers, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.accelerator_manufacturer

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.accelerator_manufacturer.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> AcceleratorManufacturers:
    import capo_auto_scaling.types.accelerator_manufacturer

    out: AcceleratorManufacturers = []
    for child in parent.findall(tag):
        out.append(
            capo_auto_scaling.types.accelerator_manufacturer.deserialize_query(child)
        )
    return out
