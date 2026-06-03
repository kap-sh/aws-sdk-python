"""Generated from Smithy shape ``com.amazonaws.secretsmanager#UntagResource``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_secrets_manager._auth._signers
from aws_sdk_secrets_manager._services._pipeline import (
    AsyncOperationOptions,
    OperationOptions,
)

if TYPE_CHECKING:
    import aws_sdk_secrets_manager.types.untag_resource_request


def untag_resource(
    options: OperationOptions,
    input: aws_sdk_secrets_manager.types.untag_resource_request.UntagResourceRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_untag_resource(
    options: AsyncOperationOptions,
    input: aws_sdk_secrets_manager.types.untag_resource_request.UntagResourceRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
