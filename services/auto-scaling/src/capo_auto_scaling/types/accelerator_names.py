"""Generated from Smithy shape ``com.amazonaws.autoscaling#AcceleratorNames``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.accelerator_name

AcceleratorNames: TypeAlias = list[
    "capo_auto_scaling.types.accelerator_name.AcceleratorName"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: AcceleratorNames, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.accelerator_name

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.accelerator_name.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> AcceleratorNames:
    import capo_auto_scaling.types.accelerator_name

    out: AcceleratorNames = []
    for child in el.findall("member"):
        out.append(capo_auto_scaling.types.accelerator_name.deserialize_query(child))
    return out


def serialize_query_flat(
    value: AcceleratorNames, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.accelerator_name

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.accelerator_name.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> AcceleratorNames:
    import capo_auto_scaling.types.accelerator_name

    out: AcceleratorNames = []
    for child in parent.findall(tag):
        out.append(capo_auto_scaling.types.accelerator_name.deserialize_query(child))
    return out
