"""Generated from Smithy shape ``com.amazonaws.ec2#MacHost``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.dedicated_host_id
    import aws_sdk_ec2.types.mac_os_version_string_list


class MacHost(TypedDict):
    host_id: NotRequired["aws_sdk_ec2.types.dedicated_host_id.DedicatedHostId"]
    """<p> The EC2 Mac Dedicated Host ID. </p>"""
    mac_os_latest_supported_versions: NotRequired[
        "aws_sdk_ec2.types.mac_os_version_string_list.MacOSVersionStringList"
    ]
    """<p> The latest macOS versions that the EC2 Mac Dedicated Host can launch without being upgraded. </p>"""
