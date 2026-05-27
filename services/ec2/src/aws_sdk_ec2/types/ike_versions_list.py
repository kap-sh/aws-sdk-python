"""Generated from Smithy shape ``com.amazonaws.ec2#IKEVersionsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.ike_versions_list_value

IKEVersionsList: TypeAlias = list[
    "aws_sdk_ec2.types.ike_versions_list_value.IKEVersionsListValue"
]
