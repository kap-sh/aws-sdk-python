"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstancesModificationResultList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.reserved_instances_modification_result

ReservedInstancesModificationResultList: TypeAlias = list[
    "capo_ec2.types.reserved_instances_modification_result.ReservedInstancesModificationResult"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReservedInstancesModificationResultList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.reserved_instances_modification_result

        capo_ec2.types.reserved_instances_modification_result.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> ReservedInstancesModificationResultList:
    import capo_ec2.types.reserved_instances_modification_result

    out: ReservedInstancesModificationResultList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.reserved_instances_modification_result.deserialize_ec2_query(
                child
            )
        )
    return out
