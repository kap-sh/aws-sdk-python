"""Generated from Smithy shape ``com.amazonaws.iam#ListAttachedRolePolicies``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.list_attached_role_policies_request
    import aws_sdk_iam.types.list_attached_role_policies_response


def list_attached_role_policies(
    options: OperationOptions,
    input: aws_sdk_iam.types.list_attached_role_policies_request.ListAttachedRolePoliciesRequest,
) -> tuple[
    aws_sdk_iam.types.list_attached_role_policies_response.ListAttachedRolePoliciesResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_attached_role_policies(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.list_attached_role_policies_request.ListAttachedRolePoliciesRequest,
) -> tuple[
    aws_sdk_iam.types.list_attached_role_policies_response.ListAttachedRolePoliciesResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
