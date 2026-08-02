"""Generated from Smithy shape ``com.amazonaws.ec2#PeeringConnectionOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean


class PeeringConnectionOptionsRequest(TypedDict, closed=True):
    allow_dns_resolution_from_remote_vpc: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>If true, enables a local VPC to resolve public DNS hostnames to private IP addresses when queried from instances in the peer VPC.</p>"""
    allow_egress_from_local_classic_link_to_remote_vpc: NotRequired[
        "capo_ec2.types.boolean.Boolean"
    ]
    """<p>Deprecated.</p>"""
    allow_egress_from_local_vpc_to_remote_classic_link: NotRequired[
        "capo_ec2.types.boolean.Boolean"
    ]
    """<p>Deprecated.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: PeeringConnectionOptionsRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "allow_dns_resolution_from_remote_vpc" in value:
        pairs.append(
            (
                f"{key_prefix}AllowDnsResolutionFromRemoteVpc",
                "true" if value["allow_dns_resolution_from_remote_vpc"] else "false",
            )
        )
    if "allow_egress_from_local_classic_link_to_remote_vpc" in value:
        pairs.append(
            (
                f"{key_prefix}AllowEgressFromLocalClassicLinkToRemoteVpc",
                "true"
                if value["allow_egress_from_local_classic_link_to_remote_vpc"]
                else "false",
            )
        )
    if "allow_egress_from_local_vpc_to_remote_classic_link" in value:
        pairs.append(
            (
                f"{key_prefix}AllowEgressFromLocalVpcToRemoteClassicLink",
                "true"
                if value["allow_egress_from_local_vpc_to_remote_classic_link"]
                else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> PeeringConnectionOptionsRequest:
    out: PeeringConnectionOptionsRequest = {}  # type: ignore[typeddict-item]
    child_allow_dns_resolution_from_remote_vpc = el.find(
        "AllowDnsResolutionFromRemoteVpc"
    )
    if child_allow_dns_resolution_from_remote_vpc is not None:
        out["allow_dns_resolution_from_remote_vpc"] = (
            child_allow_dns_resolution_from_remote_vpc.text or ""
        ).lower() == "true"
    child_allow_egress_from_local_classic_link_to_remote_vpc = el.find(
        "AllowEgressFromLocalClassicLinkToRemoteVpc"
    )
    if child_allow_egress_from_local_classic_link_to_remote_vpc is not None:
        out["allow_egress_from_local_classic_link_to_remote_vpc"] = (
            child_allow_egress_from_local_classic_link_to_remote_vpc.text or ""
        ).lower() == "true"
    child_allow_egress_from_local_vpc_to_remote_classic_link = el.find(
        "AllowEgressFromLocalVpcToRemoteClassicLink"
    )
    if child_allow_egress_from_local_vpc_to_remote_classic_link is not None:
        out["allow_egress_from_local_vpc_to_remote_classic_link"] = (
            child_allow_egress_from_local_vpc_to_remote_classic_link.text or ""
        ).lower() == "true"
    return out
