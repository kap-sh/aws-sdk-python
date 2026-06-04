"""Generated from Smithy shape ``com.amazonaws.iam#TagRole``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.tag_role_request


def tag_role(
    options: OperationOptions, input: aws_sdk_iam.types.tag_role_request.TagRoleRequest
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_tag_role(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.tag_role_request.TagRoleRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
