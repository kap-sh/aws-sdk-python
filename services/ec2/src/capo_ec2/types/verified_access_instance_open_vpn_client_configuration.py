"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessInstanceOpenVpnClientConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.string
    import capo_ec2.types.verified_access_instance_open_vpn_client_configuration_route_list


class VerifiedAccessInstanceOpenVpnClientConfiguration(TypedDict, closed=True):
    config: NotRequired["capo_ec2.types.string.String"]
    """<p>The base64-encoded Open VPN client configuration.</p>"""
    routes: NotRequired[
        "capo_ec2.types.verified_access_instance_open_vpn_client_configuration_route_list.VerifiedAccessInstanceOpenVpnClientConfigurationRouteList"
    ]
    """<p>The routes.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VerifiedAccessInstanceOpenVpnClientConfiguration,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "config" in value:
        pairs.append((f"{prefix}.Config", str(value["config"])))
    if "routes" in value:
        import capo_ec2.types.verified_access_instance_open_vpn_client_configuration_route_list

        capo_ec2.types.verified_access_instance_open_vpn_client_configuration_route_list.serialize_ec2_query(
            value["routes"], pairs, f"{prefix}.RouteSet"
        )


def deserialize_ec2_query(
    el: Element,
) -> VerifiedAccessInstanceOpenVpnClientConfiguration:
    out: VerifiedAccessInstanceOpenVpnClientConfiguration = {}  # type: ignore[typeddict-item]
    child_config = el.find("Config")
    if child_config is not None:
        out["config"] = str(child_config.text or "")
    if el.find("RouteSet") is not None:
        import capo_ec2.types.verified_access_instance_open_vpn_client_configuration_route_list

        out["routes"] = (
            capo_ec2.types.verified_access_instance_open_vpn_client_configuration_route_list.deserialize_ec2_query(
                el, "RouteSet"
            )
        )
    return out
