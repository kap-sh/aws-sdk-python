"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeSnapshotAttributeResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_volume_permission_list
    import aws_sdk_ec2.types.product_code_list
    import aws_sdk_ec2.types.string


class DescribeSnapshotAttributeResult(TypedDict):
    product_codes: NotRequired["aws_sdk_ec2.types.product_code_list.ProductCodeList"]
    """<p>The product codes.</p>"""
    snapshot_id: NotRequired["aws_sdk_ec2.types.string.String"]
    """<p>The ID of the EBS snapshot.</p>"""
    create_volume_permissions: NotRequired[
        "aws_sdk_ec2.types.create_volume_permission_list.CreateVolumePermissionList"
    ]
    """<p>The users and groups that have the permissions for creating volumes from the snapshot.</p>"""
