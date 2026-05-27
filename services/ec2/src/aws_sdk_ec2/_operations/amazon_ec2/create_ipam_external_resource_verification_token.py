"""Generated from Smithy shape ``com.amazonaws.ec2#CreateIpamExternalResourceVerificationToken``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_ipam_external_resource_verification_token_request
    import aws_sdk_ec2.types.create_ipam_external_resource_verification_token_result


def create_ipam_external_resource_verification_token(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_ipam_external_resource_verification_token_request.CreateIpamExternalResourceVerificationTokenRequest,
) -> tuple[
    aws_sdk_ec2.types.create_ipam_external_resource_verification_token_result.CreateIpamExternalResourceVerificationTokenResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_ipam_external_resource_verification_token(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_ipam_external_resource_verification_token_request.CreateIpamExternalResourceVerificationTokenRequest,
) -> tuple[
    aws_sdk_ec2.types.create_ipam_external_resource_verification_token_result.CreateIpamExternalResourceVerificationTokenResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
