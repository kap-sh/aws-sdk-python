"""Generated from Smithy shape ``com.amazonaws.ec2#CopyImageRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.copy_image_client_token
    import aws_sdk_ec2.types.image_description_request
    import aws_sdk_ec2.types.image_name_request
    import aws_sdk_ec2.types.kms_key_id
    import aws_sdk_ec2.types.long
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.tag_specification_list


class CopyImageRequest(TypedDict):
    client_token: NotRequired[
        "aws_sdk_ec2.types.copy_image_client_token.CopyImageClientToken"
    ]
    """<p>Unique, case-sensitive identifier you provide to ensure idempotency of the request. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency in Amazon EC2 API requests</a> in the <i>Amazon EC2 API Reference</i>.</p>"""
    description: NotRequired[
        "aws_sdk_ec2.types.image_description_request.ImageDescriptionRequest"
    ]
    """<p>A description for the new AMI.</p>"""
    encrypted: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Specifies whether to encrypt the snapshots of the copied image.</p> <p>You can encrypt a copy of an unencrypted snapshot, but you cannot create an unencrypted copy of an encrypted snapshot. The default KMS key for Amazon EBS is used unless you specify a non-default Key Management Service (KMS) KMS key using <code>KmsKeyId</code>. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIEncryption.html\">Use encryption with EBS-backed AMIs</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    kms_key_id: NotRequired["aws_sdk_ec2.types.kms_key_id.KmsKeyId"]
    """<p>The identifier of the symmetric Key Management Service (KMS) KMS key to use when creating encrypted volumes. If this parameter is not specified, your Amazon Web Services managed KMS key for Amazon EBS is used. If you specify a KMS key, you must also set the encrypted state to <code>true</code>.</p> <p>You can specify a KMS key using any of the following:</p> <ul> <li> <p>Key ID. For example, 1234abcd-12ab-34cd-56ef-1234567890ab.</p> </li> <li> <p>Key alias. For example, alias/ExampleAlias.</p> </li> <li> <p>Key ARN. For example, arn:aws:kms:us-east-1:012345678910:key/1234abcd-12ab-34cd-56ef-1234567890ab.</p> </li> <li> <p>Alias ARN. For example, arn:aws:kms:us-east-1:012345678910:alias/ExampleAlias.</p> </li> </ul> <p>Amazon Web Services authenticates the KMS key asynchronously. Therefore, if you specify an identifier that is not valid, the action can appear to complete, but eventually fails.</p> <p>The specified KMS key must exist in the destination Region.</p> <p>Amazon EBS does not support asymmetric KMS keys.</p>"""
    name: NotRequired["aws_sdk_ec2.types.image_name_request.ImageNameRequest"]
    """<p>The name of the new AMI.</p>"""
    source_image_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the AMI to copy.</p>"""
    source_region: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the Region that contains the AMI to copy.</p>"""
    destination_outpost_arn: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Outpost for the new AMI.</p> <p>Only specify this parameter when copying an AMI from an Amazon Web Services Region to an Outpost. The AMI must be in the Region of the destination Outpost. You can't copy an AMI from an Outpost to a Region, from one Outpost to another, or within the same Outpost.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/snapshots-outposts.html#copy-amis\">Copy AMIs from an Amazon Web Services Region to an Outpost</a> in the <i>Amazon EBS User Guide</i>.</p> <p>Only one of <code>DestinationAvailabilityZone</code>, <code>DestinationAvailabilityZoneId</code>, or <code>DestinationOutpostArn</code> can be specified.</p>"""
    copy_image_tags: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Specifies whether to copy your user-defined AMI tags to the new AMI.</p> <p>The following tags are not be copied:</p> <ul> <li> <p>System tags (prefixed with <code>aws:</code>)</p> </li> <li> <p>For public and shared AMIs, user-defined tags that are attached by other Amazon Web Services accounts</p> </li> </ul> <p>Default: Your user-defined AMI tags are not copied.</p>"""
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the new AMI and new snapshots. You can tag the AMI, the snapshots, or both.</p> <ul> <li> <p>To tag the new AMI, the value for <code>ResourceType</code> must be <code>image</code>.</p> </li> <li> <p>To tag the new snapshots, the value for <code>ResourceType</code> must be <code>snapshot</code>. The same tag is applied to all the new snapshots.</p> </li> </ul> <p>If you specify other values for <code>ResourceType</code>, the request fails.</p> <p>To tag an AMI or snapshot after it has been created, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTags.html\">CreateTags</a>.</p>"""
    snapshot_copy_completion_duration_minutes: NotRequired[
        "aws_sdk_ec2.types.long.Long"
    ]
    """<p>Specify a completion duration, in 15 minute increments, to initiate a time-based AMI copy. The specified completion duration applies to each of the snapshots associated with the AMI. Each snapshot associated with the AMI will be completed within the specified completion duration, with copy throughput automatically adjusted for each snapshot based on its size to meet the timing target.</p> <p>If you do not specify a value, the AMI copy operation is completed on a best-effort basis.</p> <note> <p>This parameter is not supported when copying an AMI to or from a Local Zone, or to an Outpost.</p> </note> <p>For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/time-based-copies.html\">Time-based copies for Amazon EBS snapshots and EBS-backed AMIs</a>.</p>"""
    destination_availability_zone: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The Local Zone for the new AMI (for example, <code>cn-north-1-pkx-1a</code>).</p> <p>Only one of <code>DestinationAvailabilityZone</code>, <code>DestinationAvailabilityZoneId</code>, or <code>DestinationOutpostArn</code> can be specified.</p>"""
    destination_availability_zone_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Local Zone for the new AMI (for example, <code>cnn1-pkx1-az1</code>).</p> <p>Only one of <code>DestinationAvailabilityZone</code>, <code>DestinationAvailabilityZoneId</code>, or <code>DestinationOutpostArn</code> can be specified.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
