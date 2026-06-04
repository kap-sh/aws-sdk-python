"""Generated from Smithy shape ``com.amazonaws.iam#ListSAMLProviders``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.list_saml_providers_request
    import aws_sdk_iam.types.list_saml_providers_response


def list_saml_providers(
    options: OperationOptions,
    input: aws_sdk_iam.types.list_saml_providers_request.ListSAMLProvidersRequest,
) -> tuple[
    aws_sdk_iam.types.list_saml_providers_response.ListSAMLProvidersResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_saml_providers(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.list_saml_providers_request.ListSAMLProvidersRequest,
) -> tuple[
    aws_sdk_iam.types.list_saml_providers_response.ListSAMLProvidersResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
