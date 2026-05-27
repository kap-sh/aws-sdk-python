"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVerifiedAccessGroup``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_verified_access_group_request
    import aws_sdk_ec2.types.create_verified_access_group_result


def create_verified_access_group(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_verified_access_group_request.CreateVerifiedAccessGroupRequest,
) -> tuple[
    aws_sdk_ec2.types.create_verified_access_group_result.CreateVerifiedAccessGroupResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_verified_access_group(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_verified_access_group_request.CreateVerifiedAccessGroupRequest,
) -> tuple[
    aws_sdk_ec2.types.create_verified_access_group_result.CreateVerifiedAccessGroupResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
