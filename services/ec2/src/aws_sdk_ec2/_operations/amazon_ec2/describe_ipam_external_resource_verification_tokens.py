"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIpamExternalResourceVerificationTokens``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_ipam_external_resource_verification_tokens_request
    import aws_sdk_ec2.types.describe_ipam_external_resource_verification_tokens_result


def describe_ipam_external_resource_verification_tokens(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_ipam_external_resource_verification_tokens_request.DescribeIpamExternalResourceVerificationTokensRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_ipam_external_resource_verification_tokens_result.DescribeIpamExternalResourceVerificationTokensResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_ipam_external_resource_verification_tokens(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_ipam_external_resource_verification_tokens_request.DescribeIpamExternalResourceVerificationTokensRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_ipam_external_resource_verification_tokens_result.DescribeIpamExternalResourceVerificationTokensResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
