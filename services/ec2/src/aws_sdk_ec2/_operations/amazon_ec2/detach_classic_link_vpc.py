"""Generated from Smithy shape ``com.amazonaws.ec2#DetachClassicLinkVpc``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.detach_classic_link_vpc_request
    import aws_sdk_ec2.types.detach_classic_link_vpc_result


def detach_classic_link_vpc(
    options: OperationOptions,
    input: aws_sdk_ec2.types.detach_classic_link_vpc_request.DetachClassicLinkVpcRequest,
) -> tuple[
    aws_sdk_ec2.types.detach_classic_link_vpc_result.DetachClassicLinkVpcResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_detach_classic_link_vpc(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.detach_classic_link_vpc_request.DetachClassicLinkVpcRequest,
) -> tuple[
    aws_sdk_ec2.types.detach_classic_link_vpc_result.DetachClassicLinkVpcResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
