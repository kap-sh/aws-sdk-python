"""Generated from Smithy shape ``com.amazonaws.iam#ListPoliciesGrantingServiceAccess``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.list_policies_granting_service_access_request
    import aws_sdk_iam.types.list_policies_granting_service_access_response


def list_policies_granting_service_access(
    options: OperationOptions,
    input: aws_sdk_iam.types.list_policies_granting_service_access_request.ListPoliciesGrantingServiceAccessRequest,
) -> tuple[
    aws_sdk_iam.types.list_policies_granting_service_access_response.ListPoliciesGrantingServiceAccessResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_policies_granting_service_access(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.list_policies_granting_service_access_request.ListPoliciesGrantingServiceAccessRequest,
) -> tuple[
    aws_sdk_iam.types.list_policies_granting_service_access_response.ListPoliciesGrantingServiceAccessResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
