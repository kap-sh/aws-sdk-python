"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVpcEncryptionControl``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_vpc_encryption_control_request
    import aws_sdk_ec2.types.create_vpc_encryption_control_result


def create_vpc_encryption_control(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_vpc_encryption_control_request.CreateVpcEncryptionControlRequest,
) -> tuple[
    aws_sdk_ec2.types.create_vpc_encryption_control_result.CreateVpcEncryptionControlResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_vpc_encryption_control(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_vpc_encryption_control_request.CreateVpcEncryptionControlRequest,
) -> tuple[
    aws_sdk_ec2.types.create_vpc_encryption_control_result.CreateVpcEncryptionControlResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
