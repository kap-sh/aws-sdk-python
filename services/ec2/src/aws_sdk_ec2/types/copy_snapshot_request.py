"""Generated from Smithy shape ``com.amazonaws.ec2#CopySnapshotRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.copy_snapshot_request_psu
    import aws_sdk_ec2.types.kms_key_id
    import aws_sdk_ec2.types.snapshot_completion_duration_minutes_request
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class CopySnapshotRequest(TypedDict):
    description: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>A description for the EBS snapshot.</p>"""
    destination_outpost_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Outpost to which to copy the snapshot.</p> <note> <p>Only supported when copying a snapshot to an Outpost.</p> </note> <p>For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/snapshots-outposts.html#copy-snapshots\"> Copy snapshots from an Amazon Web Services Region to an Outpost</a> in the <i>Amazon EBS User Guide</i>.</p>"""
    destination_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The destination Region to use in the <code>PresignedUrl</code> parameter of a snapshot copy operation. This parameter is only valid for specifying the destination Region in a <code>PresignedUrl</code> parameter, where it is required.</p> <p>The snapshot copy is sent to the regional endpoint that you sent the HTTP request to (for example, <code>ec2.us-east-1.amazonaws.com</code>). With the CLI, this is specified using the <code>--region</code> parameter or the default Region in your Amazon Web Services configuration file.</p>"""
    encrypted: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>To encrypt a copy of an unencrypted snapshot if encryption by default is not enabled, enable encryption using this parameter. Otherwise, omit this parameter. Copies of encrypted snapshots are encrypted, even if you omit this parameter and encryption by default is not enabled. You cannot set this parameter to false. For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html\">Amazon EBS encryption</a> in the <i>Amazon EBS User Guide</i>.</p>"""
    kms_key_id: NotRequired["aws_sdk_ec2.types.kms_key_id.KmsKeyId"]
    """<p>The identifier of the KMS key to use for Amazon EBS encryption. If this parameter is not specified, your KMS key for Amazon EBS is used. If <code>KmsKeyId</code> is specified, the encrypted state must be <code>true</code>.</p> <p>You can specify the KMS key using any of the following:</p> <ul> <li> <p>Key ID. For example, 1234abcd-12ab-34cd-56ef-1234567890ab.</p> </li> <li> <p>Key alias. For example, alias/ExampleAlias.</p> </li> <li> <p>Key ARN. For example, arn:aws:kms:us-east-1:012345678910:key/1234abcd-12ab-34cd-56ef-1234567890ab.</p> </li> <li> <p>Alias ARN. For example, arn:aws:kms:us-east-1:012345678910:alias/ExampleAlias.</p> </li> </ul> <p>Amazon Web Services authenticates the KMS key asynchronously. Therefore, if you specify an ID, alias, or ARN that is not valid, the action can appear to complete, but eventually fails.</p>"""
    presigned_url: NotRequired[
        "aws_sdk_ec2.types.copy_snapshot_request_psu.CopySnapshotRequestPSU"
    ]
    """<p>When you copy an encrypted source snapshot using the Amazon EC2 Query API, you must supply a pre-signed URL. This parameter is optional for unencrypted snapshots. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html\">Query requests</a>.</p> <p>The <code>PresignedUrl</code> should use the snapshot source endpoint, the <code>CopySnapshot</code> action, and include the <code>SourceRegion</code>, <code>SourceSnapshotId</code>, and <code>DestinationRegion</code> parameters. The <code>PresignedUrl</code> must be signed using Amazon Web Services Signature Version 4. Because EBS snapshots are stored in Amazon S3, the signing algorithm for this parameter uses the same logic that is described in <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-auth.html\"> Authenticating Requests: Using Query Parameters (Amazon Web Services Signature Version 4)</a> in the <i>Amazon S3 API Reference</i>. An invalid or improperly signed <code>PresignedUrl</code> will cause the copy operation to fail asynchronously, and the snapshot will move to an <code>error</code> state.</p>"""
    source_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Region that contains the snapshot to be copied.</p>"""
    source_snapshot_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the EBS snapshot to copy.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the new snapshot.</p>"""
    completion_duration_minutes: NotRequired[
        "aws_sdk_ec2.types.snapshot_completion_duration_minutes_request.SnapshotCompletionDurationMinutesRequest"
    ]
    """<note> <p>Not supported when copying snapshots to or from Local Zones or Outposts.</p> </note> <p>Specify a completion duration, in 15 minute increments, to initiate a time-based snapshot copy. Time-based snapshot copy operations complete within the specified duration. For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/time-based-copies.html\"> Time-based copies</a>.</p> <p>If you do not specify a value, the snapshot copy operation is completed on a best-effort basis.</p>"""
    destination_availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Local Zone, for example, <code>cn-north-1-pkx-1a</code> to which to copy the snapshot.</p> <note> <p>Only supported when copying a snapshot to a Local Zone.</p> </note>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
