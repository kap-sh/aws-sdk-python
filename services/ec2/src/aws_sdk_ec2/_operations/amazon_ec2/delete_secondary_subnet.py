"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteSecondarySubnet``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_secondary_subnet_request
    import aws_sdk_ec2.types.delete_secondary_subnet_result


def delete_secondary_subnet(
    options: OperationOptions,
    input: aws_sdk_ec2.types.delete_secondary_subnet_request.DeleteSecondarySubnetRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_secondary_subnet_result.DeleteSecondarySubnetResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_secondary_subnet(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.delete_secondary_subnet_request.DeleteSecondarySubnetRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_secondary_subnet_result.DeleteSecondarySubnetResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
