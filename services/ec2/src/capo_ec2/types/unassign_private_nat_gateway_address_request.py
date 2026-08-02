"""Generated from Smithy shape ``com.amazonaws.ec2#UnassignPrivateNatGatewayAddressRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.drain_seconds
    import capo_ec2.types.ip_list
    import capo_ec2.types.nat_gateway_id


class UnassignPrivateNatGatewayAddressRequest(TypedDict, closed=True):
    nat_gateway_id: NotRequired["capo_ec2.types.nat_gateway_id.NatGatewayId"]
    """<p>The ID of the NAT gateway.</p>"""
    private_ip_addresses: NotRequired["capo_ec2.types.ip_list.IpList"]
    """<p>The private IPv4 addresses you want to unassign.</p>"""
    max_drain_duration_seconds: NotRequired["capo_ec2.types.drain_seconds.DrainSeconds"]
    """<p>The maximum amount of time to wait (in seconds) before forcibly releasing the IP addresses if connections are still in progress. Default value is 350 seconds.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: UnassignPrivateNatGatewayAddressRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "nat_gateway_id" in value:
        pairs.append((f"{key_prefix}NatGatewayId", str(value["nat_gateway_id"])))
    if "private_ip_addresses" in value:
        import capo_ec2.types.ip_list

        capo_ec2.types.ip_list.serialize_ec2_query(
            value["private_ip_addresses"], pairs, f"{key_prefix}PrivateIpAddresses"
        )
    if "max_drain_duration_seconds" in value:
        pairs.append(
            (
                f"{key_prefix}MaxDrainDurationSeconds",
                str(value["max_drain_duration_seconds"]),
            )
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> UnassignPrivateNatGatewayAddressRequest:
    out: UnassignPrivateNatGatewayAddressRequest = {}  # type: ignore[typeddict-item]
    child_nat_gateway_id = el.find("NatGatewayId")
    if child_nat_gateway_id is not None:
        out["nat_gateway_id"] = str(child_nat_gateway_id.text or "")
    if el.find("PrivateIpAddresses") is not None:
        import capo_ec2.types.ip_list

        out["private_ip_addresses"] = capo_ec2.types.ip_list.deserialize_ec2_query(
            el, "PrivateIpAddresses"
        )
    child_max_drain_duration_seconds = el.find("MaxDrainDurationSeconds")
    if child_max_drain_duration_seconds is not None:
        out["max_drain_duration_seconds"] = int(
            child_max_drain_duration_seconds.text or ""
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
