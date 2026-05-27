"""Generated from Smithy shape ``com.amazonaws.ec2#AllocateAddress``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.allocate_address_request
    import aws_sdk_ec2.types.allocate_address_result


def allocate_address(
    options: OperationOptions,
    input: aws_sdk_ec2.types.allocate_address_request.AllocateAddressRequest,
) -> tuple[
    aws_sdk_ec2.types.allocate_address_result.AllocateAddressResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_allocate_address(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.allocate_address_request.AllocateAddressRequest,
) -> tuple[
    aws_sdk_ec2.types.allocate_address_result.AllocateAddressResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
