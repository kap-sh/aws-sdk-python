"""Generated from Smithy shape ``com.amazonaws.iam#UpdateRoleDescription``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.update_role_description_request
    import aws_sdk_iam.types.update_role_description_response


def update_role_description(
    options: OperationOptions,
    input: aws_sdk_iam.types.update_role_description_request.UpdateRoleDescriptionRequest,
) -> tuple[
    aws_sdk_iam.types.update_role_description_response.UpdateRoleDescriptionResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_update_role_description(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.update_role_description_request.UpdateRoleDescriptionRequest,
) -> tuple[
    aws_sdk_iam.types.update_role_description_response.UpdateRoleDescriptionResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
