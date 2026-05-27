"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteVpcBlockPublicAccessExclusion``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_vpc_block_public_access_exclusion_request
    import aws_sdk_ec2.types.delete_vpc_block_public_access_exclusion_result


def delete_vpc_block_public_access_exclusion(
    options: OperationOptions,
    input: aws_sdk_ec2.types.delete_vpc_block_public_access_exclusion_request.DeleteVpcBlockPublicAccessExclusionRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_vpc_block_public_access_exclusion_result.DeleteVpcBlockPublicAccessExclusionResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_vpc_block_public_access_exclusion(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.delete_vpc_block_public_access_exclusion_request.DeleteVpcBlockPublicAccessExclusionRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_vpc_block_public_access_exclusion_result.DeleteVpcBlockPublicAccessExclusionResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
