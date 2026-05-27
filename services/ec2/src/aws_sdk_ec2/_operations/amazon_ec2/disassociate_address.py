"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateAddress``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disassociate_address_request


def disassociate_address(
    options: OperationOptions,
    input: aws_sdk_ec2.types.disassociate_address_request.DisassociateAddressRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_disassociate_address(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.disassociate_address_request.DisassociateAddressRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
