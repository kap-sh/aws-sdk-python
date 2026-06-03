"""Generated from Smithy shape ``com.amazonaws.kms#TagResource``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_kms._auth._signers
from aws_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_kms.types.tag_resource_request


def tag_resource(
    options: OperationOptions,
    input: aws_sdk_kms.types.tag_resource_request.TagResourceRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_tag_resource(
    options: AsyncOperationOptions,
    input: aws_sdk_kms.types.tag_resource_request.TagResourceRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
