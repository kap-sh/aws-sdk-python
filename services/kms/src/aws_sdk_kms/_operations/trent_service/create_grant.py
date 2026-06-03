"""Generated from Smithy shape ``com.amazonaws.kms#CreateGrant``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_kms._auth._signers
from aws_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_kms.types.create_grant_request
    import aws_sdk_kms.types.create_grant_response


def create_grant(
    options: OperationOptions,
    input: aws_sdk_kms.types.create_grant_request.CreateGrantRequest,
) -> tuple[
    aws_sdk_kms.types.create_grant_response.CreateGrantResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_grant(
    options: AsyncOperationOptions,
    input: aws_sdk_kms.types.create_grant_request.CreateGrantRequest,
) -> tuple[
    aws_sdk_kms.types.create_grant_response.CreateGrantResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
