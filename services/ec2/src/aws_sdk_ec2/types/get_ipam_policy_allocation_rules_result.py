"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamPolicyAllocationRulesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ipam_policy_document_set
    import aws_sdk_ec2.types.next_token


class GetIpamPolicyAllocationRulesResult(TypedDict):
    ipam_policy_documents: NotRequired[
        "aws_sdk_ec2.types.ipam_policy_document_set.IpamPolicyDocumentSet"
    ]
    """<p>The IPAM policy documents containing the allocation rules.</p> <p>Allocation rules are optional configurations within an IPAM policy that map Amazon Web Services resource types to specific IPAM pools. If no rules are defined, the resource types default to using Amazon-provided IP addresses.</p>"""
    next_token: NotRequired["aws_sdk_ec2.types.next_token.NextToken"]
    """<p>The token to use to retrieve the next page of results.</p>"""
