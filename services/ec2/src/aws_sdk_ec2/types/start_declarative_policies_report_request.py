"""Generated from Smithy shape ``com.amazonaws.ec2#StartDeclarativePoliciesReportRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class StartDeclarativePoliciesReportRequest(TypedDict):
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    s3_bucket: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the S3 bucket where the report will be saved. The bucket must be in the same Region where the report generation request is made.</p>"""
    s3_prefix: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The prefix for your S3 object.</p>"""
    target_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The root ID, organizational unit ID, or account ID.</p> <p>Format:</p> <ul> <li> <p>For root: <code>r-ab12</code> </p> </li> <li> <p>For OU: <code>ou-ab12-cdef1234</code> </p> </li> <li> <p>For account: <code>123456789012</code> </p> </li> </ul>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply.</p>"""
