"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessInstanceOpenVpnClientConfigurationRouteList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.verified_access_instance_open_vpn_client_configuration_route

VerifiedAccessInstanceOpenVpnClientConfigurationRouteList: TypeAlias = list[
    "capo_ec2.types.verified_access_instance_open_vpn_client_configuration_route.VerifiedAccessInstanceOpenVpnClientConfigurationRoute"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VerifiedAccessInstanceOpenVpnClientConfigurationRouteList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.verified_access_instance_open_vpn_client_configuration_route

        capo_ec2.types.verified_access_instance_open_vpn_client_configuration_route.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    el: Element,
) -> VerifiedAccessInstanceOpenVpnClientConfigurationRouteList:
    import capo_ec2.types.verified_access_instance_open_vpn_client_configuration_route

    out: VerifiedAccessInstanceOpenVpnClientConfigurationRouteList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.verified_access_instance_open_vpn_client_configuration_route.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> VerifiedAccessInstanceOpenVpnClientConfigurationRouteList:
    import capo_ec2.types.verified_access_instance_open_vpn_client_configuration_route

    out: VerifiedAccessInstanceOpenVpnClientConfigurationRouteList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.verified_access_instance_open_vpn_client_configuration_route.deserialize_ec2_query(
                child
            )
        )
    return out
