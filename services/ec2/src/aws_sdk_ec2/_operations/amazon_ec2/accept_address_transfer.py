"""Generated from Smithy shape ``com.amazonaws.ec2#AcceptAddressTransfer``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.accept_address_transfer_request
    import aws_sdk_ec2.types.accept_address_transfer_result


def accept_address_transfer(
    options: OperationOptions,
    input: aws_sdk_ec2.types.accept_address_transfer_request.AcceptAddressTransferRequest,
) -> tuple[
    aws_sdk_ec2.types.accept_address_transfer_result.AcceptAddressTransferResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_accept_address_transfer(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.accept_address_transfer_request.AcceptAddressTransferRequest,
) -> tuple[
    aws_sdk_ec2.types.accept_address_transfer_result.AcceptAddressTransferResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
