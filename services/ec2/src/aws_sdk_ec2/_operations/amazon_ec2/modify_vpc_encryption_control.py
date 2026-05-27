"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVpcEncryptionControl``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_vpc_encryption_control_request
    import aws_sdk_ec2.types.modify_vpc_encryption_control_result


def modify_vpc_encryption_control(
    options: OperationOptions,
    input: aws_sdk_ec2.types.modify_vpc_encryption_control_request.ModifyVpcEncryptionControlRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_vpc_encryption_control_result.ModifyVpcEncryptionControlResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_modify_vpc_encryption_control(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.modify_vpc_encryption_control_request.ModifyVpcEncryptionControlRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_vpc_encryption_control_result.ModifyVpcEncryptionControlResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
