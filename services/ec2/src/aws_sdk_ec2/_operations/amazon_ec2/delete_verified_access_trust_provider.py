"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteVerifiedAccessTrustProvider``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_verified_access_trust_provider_request
    import aws_sdk_ec2.types.delete_verified_access_trust_provider_result


def delete_verified_access_trust_provider(
    options: OperationOptions,
    input: aws_sdk_ec2.types.delete_verified_access_trust_provider_request.DeleteVerifiedAccessTrustProviderRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_verified_access_trust_provider_result.DeleteVerifiedAccessTrustProviderResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_verified_access_trust_provider(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.delete_verified_access_trust_provider_request.DeleteVerifiedAccessTrustProviderRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_verified_access_trust_provider_result.DeleteVerifiedAccessTrustProviderResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
