"""Generated from Smithy shape ``com.amazonaws.ec2#PrincipalIdFormatList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.principal_id_format

PrincipalIdFormatList: TypeAlias = list[
    "aws_sdk_ec2.types.principal_id_format.PrincipalIdFormat"
]
