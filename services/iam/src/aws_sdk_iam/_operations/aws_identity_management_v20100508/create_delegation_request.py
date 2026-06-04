"""Generated from Smithy shape ``com.amazonaws.iam#CreateDelegationRequest``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.create_delegation_request_request
    import aws_sdk_iam.types.create_delegation_request_response


def create_delegation_request(
    options: OperationOptions,
    input: aws_sdk_iam.types.create_delegation_request_request.CreateDelegationRequestRequest,
) -> tuple[
    aws_sdk_iam.types.create_delegation_request_response.CreateDelegationRequestResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_delegation_request(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.create_delegation_request_request.CreateDelegationRequestRequest,
) -> tuple[
    aws_sdk_iam.types.create_delegation_request_response.CreateDelegationRequestResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
