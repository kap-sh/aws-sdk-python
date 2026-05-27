"""Generated from Smithy shape ``com.amazonaws.ec2#CreateSecurityGroup``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_security_group_request
    import aws_sdk_ec2.types.create_security_group_result


def create_security_group(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_security_group_request.CreateSecurityGroupRequest,
) -> tuple[
    aws_sdk_ec2.types.create_security_group_result.CreateSecurityGroupResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_security_group(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_security_group_request.CreateSecurityGroupRequest,
) -> tuple[
    aws_sdk_ec2.types.create_security_group_result.CreateSecurityGroupResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
