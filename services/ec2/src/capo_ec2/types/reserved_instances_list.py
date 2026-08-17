"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstancesList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.reserved_instances

ReservedInstancesList: TypeAlias = list[
    "capo_ec2.types.reserved_instances.ReservedInstances"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReservedInstancesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.reserved_instances

        capo_ec2.types.reserved_instances.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> ReservedInstancesList:
    import capo_ec2.types.reserved_instances

    out: ReservedInstancesList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.reserved_instances.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> ReservedInstancesList:
    import capo_ec2.types.reserved_instances

    out: ReservedInstancesList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.reserved_instances.deserialize_ec2_query(child))
    return out
