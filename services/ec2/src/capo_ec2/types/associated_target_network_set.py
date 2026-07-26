"""Generated from Smithy shape ``com.amazonaws.ec2#AssociatedTargetNetworkSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.associated_target_network

AssociatedTargetNetworkSet: TypeAlias = list[
    "capo_ec2.types.associated_target_network.AssociatedTargetNetwork"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AssociatedTargetNetworkSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.associated_target_network

        capo_ec2.types.associated_target_network.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> AssociatedTargetNetworkSet:
    import capo_ec2.types.associated_target_network

    out: AssociatedTargetNetworkSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.associated_target_network.deserialize_ec2_query(child)
        )
    return out
