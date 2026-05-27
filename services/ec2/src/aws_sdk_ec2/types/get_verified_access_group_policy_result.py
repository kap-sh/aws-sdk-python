"""Generated from Smithy shape ``com.amazonaws.ec2#GetVerifiedAccessGroupPolicyResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string


class GetVerifiedAccessGroupPolicyResult(TypedDict):
    policy_enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>The status of the Verified Access policy.</p>"""
    policy_document: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Verified Access policy document.</p>"""
