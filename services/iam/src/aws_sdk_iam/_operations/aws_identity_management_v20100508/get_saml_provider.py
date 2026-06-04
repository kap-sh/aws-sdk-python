"""Generated from Smithy shape ``com.amazonaws.iam#GetSAMLProvider``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.get_saml_provider_request
    import aws_sdk_iam.types.get_saml_provider_response


def get_saml_provider(
    options: OperationOptions,
    input: aws_sdk_iam.types.get_saml_provider_request.GetSAMLProviderRequest,
) -> tuple[
    aws_sdk_iam.types.get_saml_provider_response.GetSAMLProviderResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_saml_provider(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.get_saml_provider_request.GetSAMLProviderRequest,
) -> tuple[
    aws_sdk_iam.types.get_saml_provider_response.GetSAMLProviderResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
