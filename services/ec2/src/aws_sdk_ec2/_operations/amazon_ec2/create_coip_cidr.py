"""Generated from Smithy shape ``com.amazonaws.ec2#CreateCoipCidr``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_coip_cidr_request
    import aws_sdk_ec2.types.create_coip_cidr_result


def create_coip_cidr(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_coip_cidr_request.CreateCoipCidrRequest,
) -> tuple[
    aws_sdk_ec2.types.create_coip_cidr_result.CreateCoipCidrResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_coip_cidr(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_coip_cidr_request.CreateCoipCidrRequest,
) -> tuple[
    aws_sdk_ec2.types.create_coip_cidr_result.CreateCoipCidrResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
