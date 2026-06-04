"""Generated from Smithy shape ``com.amazonaws.iam#AcceptDelegationRequest``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.accept_delegation_request_request


def accept_delegation_request(
    options: OperationOptions,
    input: aws_sdk_iam.types.accept_delegation_request_request.AcceptDelegationRequestRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_accept_delegation_request(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.accept_delegation_request_request.AcceptDelegationRequestRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
