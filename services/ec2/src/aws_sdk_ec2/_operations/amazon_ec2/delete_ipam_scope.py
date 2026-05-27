"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteIpamScope``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_ipam_scope_request
    import aws_sdk_ec2.types.delete_ipam_scope_result


def delete_ipam_scope(
    options: OperationOptions,
    input: aws_sdk_ec2.types.delete_ipam_scope_request.DeleteIpamScopeRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_ipam_scope_result.DeleteIpamScopeResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_ipam_scope(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.delete_ipam_scope_request.DeleteIpamScopeRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_ipam_scope_result.DeleteIpamScopeResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
