"""Generated from Smithy shape ``com.amazonaws.iam#ListInstanceProfilesForRole``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.list_instance_profiles_for_role_request
    import aws_sdk_iam.types.list_instance_profiles_for_role_response


def list_instance_profiles_for_role(
    options: OperationOptions,
    input: aws_sdk_iam.types.list_instance_profiles_for_role_request.ListInstanceProfilesForRoleRequest,
) -> tuple[
    aws_sdk_iam.types.list_instance_profiles_for_role_response.ListInstanceProfilesForRoleResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_instance_profiles_for_role(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.list_instance_profiles_for_role_request.ListInstanceProfilesForRoleRequest,
) -> tuple[
    aws_sdk_iam.types.list_instance_profiles_for_role_response.ListInstanceProfilesForRoleResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
