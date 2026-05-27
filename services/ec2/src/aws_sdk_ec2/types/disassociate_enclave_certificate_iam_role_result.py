"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateEnclaveCertificateIamRoleResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ec2.types.boolean

DisassociateEnclaveCertificateIamRoleResult = TypedDict(
    "DisassociateEnclaveCertificateIamRoleResult",
    {
        "return": NotRequired["aws_sdk_ec2.types.boolean.Boolean"],
    },
)
