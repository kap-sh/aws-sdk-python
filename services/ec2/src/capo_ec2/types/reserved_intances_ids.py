"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedIntancesIds``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.reserved_instances_id

ReservedIntancesIds: TypeAlias = list[
    "capo_ec2.types.reserved_instances_id.ReservedInstancesId"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReservedIntancesIds, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.reserved_instances_id

        capo_ec2.types.reserved_instances_id.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> ReservedIntancesIds:
    import capo_ec2.types.reserved_instances_id

    out: ReservedIntancesIds = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.reserved_instances_id.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> ReservedIntancesIds:
    import capo_ec2.types.reserved_instances_id

    out: ReservedIntancesIds = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.reserved_instances_id.deserialize_ec2_query(child))
    return out
