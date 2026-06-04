"""Generated from Smithy shape ``com.amazonaws.iam#GenerateServiceLastAccessedDetails``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.generate_service_last_accessed_details_request
    import aws_sdk_iam.types.generate_service_last_accessed_details_response


def generate_service_last_accessed_details(
    options: OperationOptions,
    input: aws_sdk_iam.types.generate_service_last_accessed_details_request.GenerateServiceLastAccessedDetailsRequest,
) -> tuple[
    aws_sdk_iam.types.generate_service_last_accessed_details_response.GenerateServiceLastAccessedDetailsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_generate_service_last_accessed_details(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.generate_service_last_accessed_details_request.GenerateServiceLastAccessedDetailsRequest,
) -> tuple[
    aws_sdk_iam.types.generate_service_last_accessed_details_response.GenerateServiceLastAccessedDetailsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
