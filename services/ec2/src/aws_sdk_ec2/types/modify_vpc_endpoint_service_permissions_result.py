"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpcEndpointServicePermissionsResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.added_principal_set
    import aws_sdk_ec2.types.boolean


class ModifyVpcEndpointServicePermissionsResult(TypedDict):
    added_principals: NotRequired[
        "aws_sdk_ec2.types.added_principal_set.AddedPrincipalSet"
    ]
    """<p>Information about the added principals.</p>"""
    return_value: NotRequired["aws_sdk_ec2.types.boolean.Boolean"]
    """<p>Returns <code>true</code> if the request succeeds; otherwise, it returns an error.</p>"""
