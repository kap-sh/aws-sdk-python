"""Generated from Smithy shape ``com.amazonaws.ec2#Ipv6PrefixListResponse``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipv6_prefix_specification_response

Ipv6PrefixListResponse: TypeAlias = list[
    "capo_ec2.types.ipv6_prefix_specification_response.Ipv6PrefixSpecificationResponse"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Ipv6PrefixListResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.ipv6_prefix_specification_response

        capo_ec2.types.ipv6_prefix_specification_response.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> Ipv6PrefixListResponse:
    import capo_ec2.types.ipv6_prefix_specification_response

    out: Ipv6PrefixListResponse = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.ipv6_prefix_specification_response.deserialize_ec2_query(
                child
            )
        )
    return out
