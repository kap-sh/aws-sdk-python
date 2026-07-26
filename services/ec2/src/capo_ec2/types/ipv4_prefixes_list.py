"""Generated from Smithy shape ``com.amazonaws.ec2#Ipv4PrefixesList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipv4_prefix_specification

Ipv4PrefixesList: TypeAlias = list[
    "capo_ec2.types.ipv4_prefix_specification.Ipv4PrefixSpecification"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Ipv4PrefixesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.ipv4_prefix_specification

        capo_ec2.types.ipv4_prefix_specification.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> Ipv4PrefixesList:
    import capo_ec2.types.ipv4_prefix_specification

    out: Ipv4PrefixesList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.ipv4_prefix_specification.deserialize_ec2_query(child)
        )
    return out
