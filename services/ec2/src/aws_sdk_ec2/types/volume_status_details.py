"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeStatusDetails``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.string
    import aws_sdk_ec2.types.volume_status_name


class VolumeStatusDetails(TypedDict):
    name: NotRequired["aws_sdk_ec2.types.volume_status_name.VolumeStatusName"]
    """<p>The name of the volume status.</p> <ul> <li> <p> <code>io-enabled</code> - Indicates the volume I/O status. For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/monitoring-volume-checks.html\">Amazon EBS volume status checks</a>.</p> </li> <li> <p> <code>io-performance</code> - Indicates the volume performance status. For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/monitoring-volume-checks.html\">Amazon EBS volume status checks</a>.</p> </li> <li> <p> <code>initialization-state</code> - Indicates the status of the volume initialization process. For more information, see <a href=\"https://docs.aws.amazon.com/ebs/latest/userguide/initalize-volume.html\">Initialize Amazon EBS volumes</a>.</p> </li> </ul>"""
    status: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The intended status of the volume status.</p>"""
