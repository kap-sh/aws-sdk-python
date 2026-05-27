"""Generated from Smithy shape ``com.amazonaws.ec2#GetVpcResourcesBlockingEncryptionEnforcement``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_vpc_resources_blocking_encryption_enforcement_request
    import aws_sdk_ec2.types.get_vpc_resources_blocking_encryption_enforcement_result


def get_vpc_resources_blocking_encryption_enforcement(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_vpc_resources_blocking_encryption_enforcement_request.GetVpcResourcesBlockingEncryptionEnforcementRequest,
) -> tuple[
    aws_sdk_ec2.types.get_vpc_resources_blocking_encryption_enforcement_result.GetVpcResourcesBlockingEncryptionEnforcementResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_vpc_resources_blocking_encryption_enforcement(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_vpc_resources_blocking_encryption_enforcement_request.GetVpcResourcesBlockingEncryptionEnforcementRequest,
) -> tuple[
    aws_sdk_ec2.types.get_vpc_resources_blocking_encryption_enforcement_result.GetVpcResourcesBlockingEncryptionEnforcementResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
