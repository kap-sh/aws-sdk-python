"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyHostsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.auto_placement
    import aws_sdk_ec2.types.host_maintenance
    import aws_sdk_ec2.types.host_recovery
    import aws_sdk_ec2.types.request_host_id_list
    import aws_sdk_ec2.types.string


class ModifyHostsRequest(TypedDict):
    host_recovery: NotRequired["aws_sdk_ec2.types.host_recovery.HostRecovery"]
    """<p>Indicates whether to enable or disable host recovery for the Dedicated Host. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-recovery.html\">Host recovery</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    instance_type: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Specifies the instance type to be supported by the Dedicated Host. Specify this parameter to modify a Dedicated Host to support only a specific instance type.</p> <p>If you want to modify a Dedicated Host to support multiple instance types in its current instance family, omit this parameter and specify <b>InstanceFamily</b> instead. You cannot specify <b>InstanceType</b> and <b>InstanceFamily</b> in the same request.</p>"""
    instance_family: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>Specifies the instance family to be supported by the Dedicated Host. Specify this parameter to modify a Dedicated Host to support multiple instance types within its current instance family.</p> <p>If you want to modify a Dedicated Host to support a specific instance type only, omit this parameter and specify <b>InstanceType</b> instead. You cannot specify <b>InstanceFamily</b> and <b>InstanceType</b> in the same request.</p>"""
    host_maintenance: NotRequired["aws_sdk_ec2.types.host_maintenance.HostMaintenance"]
    """<p>Indicates whether to enable or disable host maintenance for the Dedicated Host. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-maintenance.html\">Host maintenance</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    host_ids: NotRequired["aws_sdk_ec2.types.request_host_id_list.RequestHostIdList"]
    """<p>The IDs of the Dedicated Hosts to modify.</p>"""
    auto_placement: NotRequired["aws_sdk_ec2.types.auto_placement.AutoPlacement"]
    """<p>Specify whether to enable or disable auto-placement.</p>"""
