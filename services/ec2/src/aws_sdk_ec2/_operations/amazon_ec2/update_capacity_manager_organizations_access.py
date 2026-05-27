"""Generated from Smithy shape ``com.amazonaws.ec2#UpdateCapacityManagerOrganizationsAccess``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.update_capacity_manager_organizations_access_request
    import aws_sdk_ec2.types.update_capacity_manager_organizations_access_result


def update_capacity_manager_organizations_access(
    options: OperationOptions,
    input: aws_sdk_ec2.types.update_capacity_manager_organizations_access_request.UpdateCapacityManagerOrganizationsAccessRequest,
) -> tuple[
    aws_sdk_ec2.types.update_capacity_manager_organizations_access_result.UpdateCapacityManagerOrganizationsAccessResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_update_capacity_manager_organizations_access(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.update_capacity_manager_organizations_access_request.UpdateCapacityManagerOrganizationsAccessRequest,
) -> tuple[
    aws_sdk_ec2.types.update_capacity_manager_organizations_access_result.UpdateCapacityManagerOrganizationsAccessResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
