"""Generated from Smithy shape ``com.amazonaws.ec2#PrivateDnsDetailsSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.private_dns_details

PrivateDnsDetailsSet: TypeAlias = list[
    "capo_ec2.types.private_dns_details.PrivateDnsDetails"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PrivateDnsDetailsSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.private_dns_details

        capo_ec2.types.private_dns_details.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> PrivateDnsDetailsSet:
    import capo_ec2.types.private_dns_details

    out: PrivateDnsDetailsSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.private_dns_details.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> PrivateDnsDetailsSet:
    import capo_ec2.types.private_dns_details

    out: PrivateDnsDetailsSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.private_dns_details.deserialize_ec2_query(child))
    return out
