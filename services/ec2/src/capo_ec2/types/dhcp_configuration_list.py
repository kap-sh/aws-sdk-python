"""Generated from Smithy shape ``com.amazonaws.ec2#DhcpConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.dhcp_configuration

DhcpConfigurationList: TypeAlias = list[
    "capo_ec2.types.dhcp_configuration.DhcpConfiguration"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DhcpConfigurationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.dhcp_configuration

        capo_ec2.types.dhcp_configuration.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> DhcpConfigurationList:
    import capo_ec2.types.dhcp_configuration

    out: DhcpConfigurationList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.dhcp_configuration.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> DhcpConfigurationList:
    import capo_ec2.types.dhcp_configuration

    out: DhcpConfigurationList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.dhcp_configuration.deserialize_ec2_query(child))
    return out
