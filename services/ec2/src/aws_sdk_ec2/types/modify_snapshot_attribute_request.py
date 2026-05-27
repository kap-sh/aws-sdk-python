"""Generated from Smithy shape ``com.amazonaws.ec2#ModifySnapshotAttributeRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean
    import aws_sdk_ec2.types.create_volume_permission_modifications
    import aws_sdk_ec2.types.group_name_string_list
    import aws_sdk_ec2.types.operation_type
    import aws_sdk_ec2.types.snapshot_attribute_name
    import aws_sdk_ec2.types.snapshot_id
    import aws_sdk_ec2.types.user_id_string_list


class ModifySnapshotAttributeRequest(TypedDict):
    attribute: NotRequired[
        "aws_sdk_ec2.types.snapshot_attribute_name.SnapshotAttributeName"
    ]
    """<p>The snapshot attribute to modify. Only volume creation permissions can be modified.</p>"""
    create_volume_permission: NotRequired[
        "aws_sdk_ec2.types.create_volume_permission_modifications.CreateVolumePermissionModifications"
    ]
    """<p>A JSON representation of the snapshot attribute modification.</p>"""
    group_names: NotRequired[
        "aws_sdk_ec2.types.group_name_string_list.GroupNameStringList"
    ]
    """<p>The group to modify for the snapshot.</p>"""
    operation_type: NotRequired["aws_sdk_ec2.types.operation_type.OperationType"]
    """<p>The type of operation to perform to the attribute.</p>"""
    snapshot_id: NotRequired["aws_sdk_ec2.types.snapshot_id.SnapshotId"]
    """<p>The ID of the snapshot.</p>"""
    user_ids: NotRequired["aws_sdk_ec2.types.user_id_string_list.UserIdStringList"]
    """<p>The account ID to modify for the snapshot.</p>"""
    dry_run: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
