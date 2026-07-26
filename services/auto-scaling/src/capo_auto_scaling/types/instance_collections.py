"""Generated from Smithy shape ``com.amazonaws.autoscaling#InstanceCollections``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.instance_collection

InstanceCollections: TypeAlias = list[
    "capo_auto_scaling.types.instance_collection.InstanceCollection"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: InstanceCollections, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.instance_collection

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.instance_collection.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> InstanceCollections:
    import capo_auto_scaling.types.instance_collection

    out: InstanceCollections = []
    for child in el.findall("member"):
        out.append(capo_auto_scaling.types.instance_collection.deserialize_query(child))
    return out


def serialize_query_flat(
    value: InstanceCollections, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_auto_scaling.types.instance_collection

    for n, item in enumerate(value, 1):
        capo_auto_scaling.types.instance_collection.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> InstanceCollections:
    import capo_auto_scaling.types.instance_collection

    out: InstanceCollections = []
    for child in parent.findall(tag):
        out.append(capo_auto_scaling.types.instance_collection.deserialize_query(child))
    return out
