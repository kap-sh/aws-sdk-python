"""Generated from Smithy shape ``com.amazonaws.iam#DeleteServiceLinkedRole``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.delete_service_linked_role_request
    import aws_sdk_iam.types.delete_service_linked_role_response


def delete_service_linked_role(
    options: OperationOptions,
    input: aws_sdk_iam.types.delete_service_linked_role_request.DeleteServiceLinkedRoleRequest,
) -> tuple[
    aws_sdk_iam.types.delete_service_linked_role_response.DeleteServiceLinkedRoleResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_service_linked_role(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.delete_service_linked_role_request.DeleteServiceLinkedRoleRequest,
) -> tuple[
    aws_sdk_iam.types.delete_service_linked_role_response.DeleteServiceLinkedRoleResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
