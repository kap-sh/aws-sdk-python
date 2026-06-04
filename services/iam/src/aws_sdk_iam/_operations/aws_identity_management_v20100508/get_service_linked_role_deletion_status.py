"""Generated from Smithy shape ``com.amazonaws.iam#GetServiceLinkedRoleDeletionStatus``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.get_service_linked_role_deletion_status_request
    import aws_sdk_iam.types.get_service_linked_role_deletion_status_response


def get_service_linked_role_deletion_status(
    options: OperationOptions,
    input: aws_sdk_iam.types.get_service_linked_role_deletion_status_request.GetServiceLinkedRoleDeletionStatusRequest,
) -> tuple[
    aws_sdk_iam.types.get_service_linked_role_deletion_status_response.GetServiceLinkedRoleDeletionStatusResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_service_linked_role_deletion_status(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.get_service_linked_role_deletion_status_request.GetServiceLinkedRoleDeletionStatusRequest,
) -> tuple[
    aws_sdk_iam.types.get_service_linked_role_deletion_status_response.GetServiceLinkedRoleDeletionStatusResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
