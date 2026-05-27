"""Generated from Smithy shape ``com.amazonaws.ec2#EnableAddressTransfer``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.enable_address_transfer_request
    import aws_sdk_ec2.types.enable_address_transfer_result


def enable_address_transfer(
    options: OperationOptions,
    input: aws_sdk_ec2.types.enable_address_transfer_request.EnableAddressTransferRequest,
) -> tuple[
    aws_sdk_ec2.types.enable_address_transfer_result.EnableAddressTransferResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_enable_address_transfer(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.enable_address_transfer_request.EnableAddressTransferRequest,
) -> tuple[
    aws_sdk_ec2.types.enable_address_transfer_result.EnableAddressTransferResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
