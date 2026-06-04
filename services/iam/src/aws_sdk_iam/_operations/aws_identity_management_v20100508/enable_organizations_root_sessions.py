"""Generated from Smithy shape ``com.amazonaws.iam#EnableOrganizationsRootSessions``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.enable_organizations_root_sessions_request
    import aws_sdk_iam.types.enable_organizations_root_sessions_response


def enable_organizations_root_sessions(
    options: OperationOptions,
    input: aws_sdk_iam.types.enable_organizations_root_sessions_request.EnableOrganizationsRootSessionsRequest,
) -> tuple[
    aws_sdk_iam.types.enable_organizations_root_sessions_response.EnableOrganizationsRootSessionsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_enable_organizations_root_sessions(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.enable_organizations_root_sessions_request.EnableOrganizationsRootSessionsRequest,
) -> tuple[
    aws_sdk_iam.types.enable_organizations_root_sessions_response.EnableOrganizationsRootSessionsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
