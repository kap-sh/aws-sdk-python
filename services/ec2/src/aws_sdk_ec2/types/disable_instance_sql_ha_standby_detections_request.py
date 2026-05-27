"""Generated from Smithy shape ``com.amazonaws.ec2#DisableInstanceSqlHaStandbyDetectionsRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.instance_id_update_string_list


class DisableInstanceSqlHaStandbyDetectionsRequest(TypedDict):
    instance_ids: NotRequired[
        "aws_sdk_ec2.types.instance_id_update_string_list.InstanceIdUpdateStringList"
    ]
    """<p>The IDs of the instances to disable from SQL Server High Availability standby detection monitoring.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
