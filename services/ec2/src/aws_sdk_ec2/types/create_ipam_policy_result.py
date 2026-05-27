"""Generated from Smithy shape ``com.amazonaws.ec2#CreateIpamPolicyResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_policy


class CreateIpamPolicyResult(TypedDict):
    ipam_policy: NotRequired["aws_sdk_ec2.types.ipam_policy.IpamPolicy"]
    """<p>Information about the created IPAM policy.</p> <p>An IPAM policy is a set of rules that define how public IPv4 addresses from IPAM pools are allocated to Amazon Web Services resources. Each rule maps an Amazon Web Services service to IPAM pools that the service will use to get IP addresses. A single policy can have multiple rules and be applied to multiple Amazon Web Services Regions. If the IPAM pool run out of addresses then the services fallback to Amazon-provided IP addresses. A policy can be applied to an individual Amazon Web Services account or an entity within Amazon Web Services Organizations.</p>"""
