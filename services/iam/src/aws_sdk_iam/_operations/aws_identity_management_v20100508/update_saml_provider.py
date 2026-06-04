"""Generated from Smithy shape ``com.amazonaws.iam#UpdateSAMLProvider``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.update_saml_provider_request
    import aws_sdk_iam.types.update_saml_provider_response


def update_saml_provider(
    options: OperationOptions,
    input: aws_sdk_iam.types.update_saml_provider_request.UpdateSAMLProviderRequest,
) -> tuple[
    aws_sdk_iam.types.update_saml_provider_response.UpdateSAMLProviderResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_update_saml_provider(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.update_saml_provider_request.UpdateSAMLProviderRequest,
) -> tuple[
    aws_sdk_iam.types.update_saml_provider_response.UpdateSAMLProviderResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
