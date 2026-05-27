"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteSnapshotReturnCode``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.snapshot_id
    import aws_sdk_ec2.types.snapshot_return_codes


class DeleteSnapshotReturnCode(TypedDict):
    snapshot_id: NotRequired["aws_sdk_ec2.types.snapshot_id.SnapshotId"]
    """<p>The ID of the snapshot.</p>"""
    return_code: NotRequired[
        "aws_sdk_ec2.types.snapshot_return_codes.SnapshotReturnCodes"
    ]
    """<p>The result code from the snapshot deletion attempt. Possible values:</p> <ul> <li> <p> <code>success</code> - The snapshot was successfully deleted.</p> </li> <li> <p> <code>skipped</code> - The snapshot was not deleted because it's associated with other AMIs.</p> </li> <li> <p> <code>missing-permissions</code> - The snapshot was not deleted because the role lacks <code>DeleteSnapshot</code> permissions. For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/security_iam_service-with-iam.html\">How Amazon EBS works with IAM</a>.</p> </li> <li> <p> <code>internal-error</code> - The snapshot was not deleted due to a server error.</p> </li> <li> <p> <code>client-error</code> - The snapshot was not deleted due to a client configuration error.</p> </li> </ul> <p>For details about an error, check the <code>DeleteSnapshot</code> event in the CloudTrail event history. For more information, see <a href=\"https://docs.aws.amazon.com/awscloudtrail/latest/userguide/tutorial-event-history.html\">View event history</a> in the <i>Amazon Web Services CloudTrail User Guide</i>.</p>"""
