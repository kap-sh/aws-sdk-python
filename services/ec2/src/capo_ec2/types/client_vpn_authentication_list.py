"""Generated from Smithy shape ``com.amazonaws.ec2#ClientVpnAuthenticationList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.client_vpn_authentication

ClientVpnAuthenticationList: TypeAlias = list[
    "capo_ec2.types.client_vpn_authentication.ClientVpnAuthentication"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ClientVpnAuthenticationList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.client_vpn_authentication

        capo_ec2.types.client_vpn_authentication.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> ClientVpnAuthenticationList:
    import capo_ec2.types.client_vpn_authentication

    out: ClientVpnAuthenticationList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.client_vpn_authentication.deserialize_ec2_query(child)
        )
    return out
