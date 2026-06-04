"""Generated from Smithy shape ``com.amazonaws.iam#CreateGroup``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.create_group_request
    import aws_sdk_iam.types.create_group_response


def create_group(
    options: OperationOptions,
    input: aws_sdk_iam.types.create_group_request.CreateGroupRequest,
) -> tuple[
    aws_sdk_iam.types.create_group_response.CreateGroupResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_group(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.create_group_request.CreateGroupRequest,
) -> tuple[
    aws_sdk_iam.types.create_group_response.CreateGroupResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
