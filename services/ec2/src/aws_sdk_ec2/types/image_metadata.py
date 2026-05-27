"""Generated from Smithy shape ``com.amazonaws.ec2#ImageMetadata``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.image_id
    import aws_sdk_ec2.types.image_state
    import aws_sdk_ec2.types.string


class ImageMetadata(TypedDict):
    image_id: NotRequired["aws_sdk_ec2.types.image_id.ImageId"]
    """<p>The ID of the AMI.</p>"""
    name: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The name of the AMI.</p>"""
    owner_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the AMI.</p>"""
    state: NotRequired["aws_sdk_ec2.types.image_state.ImageState"]
    """<p>The current state of the AMI. If the state is <code>available</code>, the AMI is successfully registered and can be used to launch an instance.</p>"""
    image_owner_alias: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The alias of the AMI owner.</p> <p>Valid values: <code>amazon</code> | <code>aws-backup-vault</code> | <code>aws-marketplace</code> </p>"""
    creation_date: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The date and time the AMI was created.</p>"""
    deprecation_time: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The deprecation date and time of the AMI, in UTC, in the following format: <i>YYYY</i>-<i>MM</i>-<i>DD</i>T<i>HH</i>:<i>MM</i>:<i>SS</i>Z.</p>"""
    image_allowed: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>If <code>true</code>, the AMI satisfies the criteria for Allowed AMIs and can be discovered and used in the account. If <code>false</code>, the AMI can't be discovered or used in the account.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-allowed-amis.html\">Control the discovery and use of AMIs in Amazon EC2 with Allowed AMIs</a> in <i>Amazon EC2 User Guide</i>.</p>"""
    is_public: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the AMI has public launch permissions. A value of <code>true</code> means this AMI has public launch permissions, while <code>false</code> means it has only implicit (AMI owner) or explicit (shared with your account) launch permissions.</p>"""
