"""Generated from Smithy shape ``com.amazonaws.ec2#ClassicLinkDnsSupportList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.classic_link_dns_support

ClassicLinkDnsSupportList: TypeAlias = list[
    "capo_ec2.types.classic_link_dns_support.ClassicLinkDnsSupport"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ClassicLinkDnsSupportList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.classic_link_dns_support

        capo_ec2.types.classic_link_dns_support.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> ClassicLinkDnsSupportList:
    import capo_ec2.types.classic_link_dns_support

    out: ClassicLinkDnsSupportList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.classic_link_dns_support.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> ClassicLinkDnsSupportList:
    import capo_ec2.types.classic_link_dns_support

    out: ClassicLinkDnsSupportList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.classic_link_dns_support.deserialize_ec2_query(child))
    return out
