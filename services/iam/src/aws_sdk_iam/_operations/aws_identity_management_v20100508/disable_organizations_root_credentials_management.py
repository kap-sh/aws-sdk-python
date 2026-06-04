"""Generated from Smithy shape ``com.amazonaws.iam#DisableOrganizationsRootCredentialsManagement``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.disable_organizations_root_credentials_management_request
    import aws_sdk_iam.types.disable_organizations_root_credentials_management_response


def disable_organizations_root_credentials_management(
    options: OperationOptions,
    input: aws_sdk_iam.types.disable_organizations_root_credentials_management_request.DisableOrganizationsRootCredentialsManagementRequest,
) -> tuple[
    aws_sdk_iam.types.disable_organizations_root_credentials_management_response.DisableOrganizationsRootCredentialsManagementResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_disable_organizations_root_credentials_management(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.disable_organizations_root_credentials_management_request.DisableOrganizationsRootCredentialsManagementRequest,
) -> tuple[
    aws_sdk_iam.types.disable_organizations_root_credentials_management_response.DisableOrganizationsRootCredentialsManagementResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
