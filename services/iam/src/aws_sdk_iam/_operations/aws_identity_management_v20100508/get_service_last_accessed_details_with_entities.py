"""Generated from Smithy shape ``com.amazonaws.iam#GetServiceLastAccessedDetailsWithEntities``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.get_service_last_accessed_details_with_entities_request
    import aws_sdk_iam.types.get_service_last_accessed_details_with_entities_response


def get_service_last_accessed_details_with_entities(
    options: OperationOptions,
    input: aws_sdk_iam.types.get_service_last_accessed_details_with_entities_request.GetServiceLastAccessedDetailsWithEntitiesRequest,
) -> tuple[
    aws_sdk_iam.types.get_service_last_accessed_details_with_entities_response.GetServiceLastAccessedDetailsWithEntitiesResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_service_last_accessed_details_with_entities(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.get_service_last_accessed_details_with_entities_request.GetServiceLastAccessedDetailsWithEntitiesRequest,
) -> tuple[
    aws_sdk_iam.types.get_service_last_accessed_details_with_entities_response.GetServiceLastAccessedDetailsWithEntitiesResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
