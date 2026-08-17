"""Generated from Smithy shape ``com.amazonaws.ec2#Ipv4PrefixListResponse``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.ipv4_prefix_specification_response

Ipv4PrefixListResponse: TypeAlias = list[
    "capo_ec2.types.ipv4_prefix_specification_response.Ipv4PrefixSpecificationResponse"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Ipv4PrefixListResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.ipv4_prefix_specification_response

        capo_ec2.types.ipv4_prefix_specification_response.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> Ipv4PrefixListResponse:
    import capo_ec2.types.ipv4_prefix_specification_response

    out: Ipv4PrefixListResponse = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.ipv4_prefix_specification_response.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> Ipv4PrefixListResponse:
    import capo_ec2.types.ipv4_prefix_specification_response

    out: Ipv4PrefixListResponse = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.ipv4_prefix_specification_response.deserialize_ec2_query(
                child
            )
        )
    return out
