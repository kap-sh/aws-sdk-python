"""Generated from Smithy shape ``com.amazonaws.iam#GetDelegationRequest``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.get_delegation_request_request
    import aws_sdk_iam.types.get_delegation_request_response


def get_delegation_request(
    options: OperationOptions,
    input: aws_sdk_iam.types.get_delegation_request_request.GetDelegationRequestRequest,
) -> tuple[
    aws_sdk_iam.types.get_delegation_request_response.GetDelegationRequestResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_delegation_request(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.get_delegation_request_request.GetDelegationRequestRequest,
) -> tuple[
    aws_sdk_iam.types.get_delegation_request_response.GetDelegationRequestResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
