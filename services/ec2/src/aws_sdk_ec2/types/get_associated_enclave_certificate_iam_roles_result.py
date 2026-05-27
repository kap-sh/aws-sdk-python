"""Generated from Smithy shape ``com.amazonaws.ec2#GetAssociatedEnclaveCertificateIamRolesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.associated_roles_list


class GetAssociatedEnclaveCertificateIamRolesResult(TypedDict):
    associated_roles: NotRequired[
        "aws_sdk_ec2.types.associated_roles_list.AssociatedRolesList"
    ]
    """<p>Information about the associated IAM roles.</p>"""
