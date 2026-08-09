"""Generated from Smithy shape ``com.amazonaws.ec2#ClientVpnConnectionSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.client_vpn_connection

ClientVpnConnectionSet: TypeAlias = list[
    "capo_ec2.types.client_vpn_connection.ClientVpnConnection"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ClientVpnConnectionSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.client_vpn_connection

        capo_ec2.types.client_vpn_connection.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> ClientVpnConnectionSet:
    import capo_ec2.types.client_vpn_connection

    out: ClientVpnConnectionSet = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.client_vpn_connection.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> ClientVpnConnectionSet:
    import capo_ec2.types.client_vpn_connection

    out: ClientVpnConnectionSet = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.client_vpn_connection.deserialize_ec2_query(child))
    return out
