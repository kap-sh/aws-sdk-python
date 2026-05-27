"""Generated from Smithy shape ``com.amazonaws.ec2#CreateDefaultVpc``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_default_vpc_request
    import aws_sdk_ec2.types.create_default_vpc_result


def create_default_vpc(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_default_vpc_request.CreateDefaultVpcRequest,
) -> tuple[
    aws_sdk_ec2.types.create_default_vpc_result.CreateDefaultVpcResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_default_vpc(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_default_vpc_request.CreateDefaultVpcRequest,
) -> tuple[
    aws_sdk_ec2.types.create_default_vpc_result.CreateDefaultVpcResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
