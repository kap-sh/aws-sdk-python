"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVerifiedAccessGroupPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.verified_access_group_id
    import aws_sdk_ec2.types.verified_access_sse_specification_request


class ModifyVerifiedAccessGroupPolicyRequest(TypedDict):
    verified_access_group_id: NotRequired[
        "aws_sdk_ec2.types.verified_access_group_id.VerifiedAccessGroupId"
    ]
    """<p>The ID of the Verified Access group.</p>"""
    policy_enabled: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>The status of the Verified Access policy.</p>"""
    policy_document: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Verified Access policy document.</p>"""
    client_token: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information, see <a href=\"https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html\">Ensuring idempotency</a>.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    sse_specification: NotRequired[
        "aws_sdk_ec2.types.verified_access_sse_specification_request.VerifiedAccessSseSpecificationRequest"
    ]
    """<p>The options for server side encryption.</p>"""
