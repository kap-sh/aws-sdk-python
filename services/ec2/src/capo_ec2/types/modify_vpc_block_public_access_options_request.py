"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpcBlockPublicAccessOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.internet_gateway_block_mode


class ModifyVpcBlockPublicAccessOptionsRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    internet_gateway_block_mode: NotRequired[
        "capo_ec2.types.internet_gateway_block_mode.InternetGatewayBlockMode"
    ]
    """<p>The mode of VPC BPA.</p> <ul> <li> <p> <code>off</code>: VPC BPA is not enabled and traffic is allowed to and from internet gateways and egress-only internet gateways in this Region.</p> </li> <li> <p> <code>block-bidirectional</code>: Block all traffic to and from internet gateways and egress-only internet gateways in this Region (except for excluded VPCs and subnets).</p> </li> <li> <p> <code>block-ingress</code>: Block all internet traffic to the VPCs in this Region (except for VPCs or subnets which are excluded). Only traffic to and from NAT gateways and egress-only internet gateways is allowed because these gateways only allow outbound connections to be established.</p> </li> </ul>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVpcBlockPublicAccessOptionsRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "internet_gateway_block_mode" in value:
        import capo_ec2.types.internet_gateway_block_mode

        capo_ec2.types.internet_gateway_block_mode.serialize_ec2_query(
            value["internet_gateway_block_mode"],
            pairs,
            f"{key_prefix}InternetGatewayBlockMode",
        )


def deserialize_ec2_query(el: Element) -> ModifyVpcBlockPublicAccessOptionsRequest:
    out: ModifyVpcBlockPublicAccessOptionsRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_internet_gateway_block_mode = el.find("InternetGatewayBlockMode")
    if child_internet_gateway_block_mode is not None:
        import capo_ec2.types.internet_gateway_block_mode

        out["internet_gateway_block_mode"] = (
            capo_ec2.types.internet_gateway_block_mode.deserialize_ec2_query(
                child_internet_gateway_block_mode
            )
        )
    return out
