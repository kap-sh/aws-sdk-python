"""Generated from Smithy shape ``com.amazonaws.ec2#AccessScopePathListRequest``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.access_scope_path_request

AccessScopePathListRequest: TypeAlias = list[
    "aws_sdk_ec2.types.access_scope_path_request.AccessScopePathRequest"
]
