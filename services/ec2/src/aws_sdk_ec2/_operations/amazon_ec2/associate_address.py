"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateAddress``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.associate_address_request
    import aws_sdk_ec2.types.associate_address_result


def associate_address(
    options: OperationOptions,
    input: aws_sdk_ec2.types.associate_address_request.AssociateAddressRequest,
) -> tuple[
    aws_sdk_ec2.types.associate_address_result.AssociateAddressResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_associate_address(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.associate_address_request.AssociateAddressRequest,
) -> tuple[
    aws_sdk_ec2.types.associate_address_result.AssociateAddressResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
