"""Generated from Smithy shape ``com.amazonaws.ec2#CreateNetworkAcl``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_network_acl_request
    import aws_sdk_ec2.types.create_network_acl_result


def create_network_acl(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_network_acl_request.CreateNetworkAclRequest,
) -> tuple[
    aws_sdk_ec2.types.create_network_acl_result.CreateNetworkAclResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_network_acl(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_network_acl_request.CreateNetworkAclRequest,
) -> tuple[
    aws_sdk_ec2.types.create_network_acl_result.CreateNetworkAclResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
