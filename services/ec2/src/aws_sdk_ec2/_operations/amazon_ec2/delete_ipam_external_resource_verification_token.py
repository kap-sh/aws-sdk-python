"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteIpamExternalResourceVerificationToken``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_ipam_external_resource_verification_token_request
    import aws_sdk_ec2.types.delete_ipam_external_resource_verification_token_result


def delete_ipam_external_resource_verification_token(
    options: OperationOptions,
    input: aws_sdk_ec2.types.delete_ipam_external_resource_verification_token_request.DeleteIpamExternalResourceVerificationTokenRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_ipam_external_resource_verification_token_result.DeleteIpamExternalResourceVerificationTokenResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_ipam_external_resource_verification_token(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.delete_ipam_external_resource_verification_token_request.DeleteIpamExternalResourceVerificationTokenRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_ipam_external_resource_verification_token_result.DeleteIpamExternalResourceVerificationTokenResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
