"""Generated from Smithy shape ``com.amazonaws.ec2#NewDhcpConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.new_dhcp_configuration

NewDhcpConfigurationList: TypeAlias = list[
    "capo_ec2.types.new_dhcp_configuration.NewDhcpConfiguration"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: NewDhcpConfigurationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.new_dhcp_configuration

        capo_ec2.types.new_dhcp_configuration.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> NewDhcpConfigurationList:
    import capo_ec2.types.new_dhcp_configuration

    out: NewDhcpConfigurationList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.new_dhcp_configuration.deserialize_ec2_query(child))
    return out
