"""Generated from Smithy shape ``com.amazonaws.ec2#AccessScopePathList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.access_scope_path

AccessScopePathList: TypeAlias = list[
    "aws_sdk_ec2.types.access_scope_path.AccessScopePath"
]
