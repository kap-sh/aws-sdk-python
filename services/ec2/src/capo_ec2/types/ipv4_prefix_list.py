"""Generated from Smithy shape ``com.amazonaws.ec2#Ipv4PrefixList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipv4_prefix_specification_request

Ipv4PrefixList: TypeAlias = list[
    "capo_ec2.types.ipv4_prefix_specification_request.Ipv4PrefixSpecificationRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Ipv4PrefixList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.ipv4_prefix_specification_request

        capo_ec2.types.ipv4_prefix_specification_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> Ipv4PrefixList:
    import capo_ec2.types.ipv4_prefix_specification_request

    out: Ipv4PrefixList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.ipv4_prefix_specification_request.deserialize_ec2_query(
                child
            )
        )
    return out
