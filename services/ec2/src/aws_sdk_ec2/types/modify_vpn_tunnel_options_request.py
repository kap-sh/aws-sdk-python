"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpnTunnelOptionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.modify_vpn_tunnel_options_specification
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.vpn_connection_id


class ModifyVpnTunnelOptionsRequest(TypedDict):
    vpn_connection_id: NotRequired[
        "aws_sdk_ec2.types.vpn_connection_id.VpnConnectionId"
    ]
    """<p>The ID of the Amazon Web Services Site-to-Site VPN connection.</p>"""
    vpn_tunnel_outside_ip_address: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The external IP address of the VPN tunnel.</p>"""
    tunnel_options: NotRequired[
        "aws_sdk_ec2.types.modify_vpn_tunnel_options_specification.ModifyVpnTunnelOptionsSpecification"
    ]
    """<p>The tunnel options to modify.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    skip_tunnel_replacement: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Choose whether or not to trigger immediate tunnel replacement. This is only applicable when turning on or off <code>EnableTunnelLifecycleControl</code>.</p> <p>Valid values: <code>True</code> | <code>False</code> </p>"""
    pre_shared_key_storage: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Specifies the storage mode for the pre-shared key (PSK). Valid values are <code>Standard</code> (stored in Site-to-Site VPN service) or <code>SecretsManager</code> (stored in Amazon Web Services Secrets Manager).</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVpnTunnelOptionsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "vpn_connection_id" in value:
        pairs.append((f"{prefix}.VpnConnectionId", str(value["vpn_connection_id"])))
    if "vpn_tunnel_outside_ip_address" in value:
        pairs.append(
            (
                f"{prefix}.VpnTunnelOutsideIpAddress",
                str(value["vpn_tunnel_outside_ip_address"]),
            )
        )
    if "tunnel_options" in value:
        import aws_sdk_ec2.types.modify_vpn_tunnel_options_specification

        aws_sdk_ec2.types.modify_vpn_tunnel_options_specification.serialize_ec2_query(
            value["tunnel_options"], pairs, f"{prefix}.TunnelOptions"
        )
    if "dry_run" in value:
        pairs.append((f"{prefix}.DryRun", "true" if value["dry_run"] else "false"))
    if "skip_tunnel_replacement" in value:
        pairs.append(
            (
                f"{prefix}.SkipTunnelReplacement",
                "true" if value["skip_tunnel_replacement"] else "false",
            )
        )
    if "pre_shared_key_storage" in value:
        pairs.append(
            (f"{prefix}.PreSharedKeyStorage", str(value["pre_shared_key_storage"]))
        )


def deserialize_ec2_query(el: Element) -> ModifyVpnTunnelOptionsRequest:
    out: ModifyVpnTunnelOptionsRequest = {}  # type: ignore[typeddict-item]
    child_vpn_connection_id = el.find("VpnConnectionId")
    if child_vpn_connection_id is not None:
        out["vpn_connection_id"] = str(child_vpn_connection_id.text or "")
    child_vpn_tunnel_outside_ip_address = el.find("VpnTunnelOutsideIpAddress")
    if child_vpn_tunnel_outside_ip_address is not None:
        out["vpn_tunnel_outside_ip_address"] = str(
            child_vpn_tunnel_outside_ip_address.text or ""
        )
    child_tunnel_options = el.find("TunnelOptions")
    if child_tunnel_options is not None:
        import aws_sdk_ec2.types.modify_vpn_tunnel_options_specification

        out["tunnel_options"] = (
            aws_sdk_ec2.types.modify_vpn_tunnel_options_specification.deserialize_ec2_query(
                child_tunnel_options
            )
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_skip_tunnel_replacement = el.find("SkipTunnelReplacement")
    if child_skip_tunnel_replacement is not None:
        out["skip_tunnel_replacement"] = (
            child_skip_tunnel_replacement.text or ""
        ).lower() == "true"
    child_pre_shared_key_storage = el.find("PreSharedKeyStorage")
    if child_pre_shared_key_storage is not None:
        out["pre_shared_key_storage"] = str(child_pre_shared_key_storage.text or "")
    return out
