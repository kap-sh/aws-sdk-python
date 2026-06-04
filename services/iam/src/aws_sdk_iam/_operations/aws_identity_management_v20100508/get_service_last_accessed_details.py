"""Generated from Smithy shape ``com.amazonaws.iam#GetServiceLastAccessedDetails``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.get_service_last_accessed_details_request
    import aws_sdk_iam.types.get_service_last_accessed_details_response


def get_service_last_accessed_details(
    options: OperationOptions,
    input: aws_sdk_iam.types.get_service_last_accessed_details_request.GetServiceLastAccessedDetailsRequest,
) -> tuple[
    aws_sdk_iam.types.get_service_last_accessed_details_response.GetServiceLastAccessedDetailsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_service_last_accessed_details(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.get_service_last_accessed_details_request.GetServiceLastAccessedDetailsRequest,
) -> tuple[
    aws_sdk_iam.types.get_service_last_accessed_details_response.GetServiceLastAccessedDetailsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
