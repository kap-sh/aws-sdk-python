"""Generated from Smithy shape ``com.amazonaws.ec2#CreateIpam``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_ipam_request
    import aws_sdk_ec2.types.create_ipam_result


def create_ipam(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_ipam_request.CreateIpamRequest,
) -> tuple[aws_sdk_ec2.types.create_ipam_result.CreateIpamResult, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_ipam(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_ipam_request.CreateIpamRequest,
) -> tuple[aws_sdk_ec2.types.create_ipam_result.CreateIpamResult, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
