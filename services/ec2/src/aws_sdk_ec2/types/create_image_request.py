"""Generated from Smithy shape ``com.amazonaws.ec2#CreateImageRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.block_device_mapping_request_list
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.image_description_request
    import aws_sdk_ec2.types.image_name_request
    import aws_sdk_ec2.types.instance_id
    import aws_sdk_ec2.types.snapshot_location_enum
    import aws_sdk_ec2.types.tag_specification_list


class CreateImageRequest(TypedDict):
    tag_specifications: NotRequired[
        "aws_sdk_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the AMI and snapshots on creation. You can tag the AMI, the snapshots, or both.</p> <ul> <li> <p>To tag the AMI, the value for <code>ResourceType</code> must be <code>image</code>.</p> </li> <li> <p>To tag the snapshots that are created of the root volume and of other Amazon EBS volumes that are attached to the instance, the value for <code>ResourceType</code> must be <code>snapshot</code>. The same tag is applied to all of the snapshots that are created.</p> </li> </ul> <p>If you specify other values for <code>ResourceType</code>, the request fails.</p> <p>To tag an AMI or snapshot after it has been created, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTags.html\">CreateTags</a>. </p>"""
    snapshot_location: NotRequired[
        "aws_sdk_ec2.types.snapshot_location_enum.SnapshotLocationEnum"
    ]
    """<note> <p>Only supported for instances in Local Zones. If the source instance is not in a Local Zone, omit this parameter.</p> </note> <p>The Amazon S3 location where the snapshots will be stored.</p> <ul> <li> <p>To create local snapshots in the same Local Zone as the source instance, specify <code>local</code>.</p> </li> <li> <p>To create regional snapshots in the parent Region of the Local Zone, specify <code>regional</code> or omit this parameter.</p> </li> </ul> <p>Default: <code>regional</code> </p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    instance_id: NotRequired["aws_sdk_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance.</p>"""
    name: NotRequired["aws_sdk_ec2.types.image_name_request.ImageNameRequest"]
    """<p>A name for the new image.</p> <p>Constraints: 3-128 alphanumeric characters, parentheses (()), square brackets ([]), spaces ( ), periods (.), slashes (/), dashes (-), single quotes ('), at-signs (@), or underscores(_)</p>"""
    description: NotRequired[
        "aws_sdk_ec2.types.image_description_request.ImageDescriptionRequest"
    ]
    """<p>A description for the new image.</p>"""
    no_reboot: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether or not the instance should be automatically rebooted before creating the image. Specify one of the following values:</p> <ul> <li> <p> <code>true</code> - The instance is not rebooted before creating the image. This creates crash-consistent snapshots that include only the data that has been written to the volumes at the time the snapshots are created. Buffered data and data in memory that has not yet been written to the volumes is not included in the snapshots.</p> </li> <li> <p> <code>false</code> - The instance is rebooted before creating the image. This ensures that all buffered data and data in memory is written to the volumes before the snapshots are created.</p> </li> </ul> <p>Default: <code>false</code> </p>"""
    block_device_mappings: NotRequired[
        "aws_sdk_ec2.types.block_device_mapping_request_list.BlockDeviceMappingRequestList"
    ]
    """<p>The block device mappings.</p> <p>When using the CreateImage action:</p> <ul> <li> <p>You can't change the volume size using the VolumeSize parameter. If you want a different volume size, you must first change the volume size of the source instance.</p> </li> <li> <p>You can't modify the encryption status of existing volumes or snapshots. To create an AMI with volumes or snapshots that have a different encryption status (for example, where the source volume and snapshots are unencrypted, and you want to create an AMI with encrypted volumes or snapshots), copy the image instead.</p> </li> <li> <p>The only option that can be changed for existing mappings or snapshots is <code>DeleteOnTermination</code>.</p> </li> </ul>"""
