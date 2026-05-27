"""Generated from Smithy shape ``com.amazonaws.ec2#EnableIpamOrganizationAdminAccount``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.enable_ipam_organization_admin_account_request
    import aws_sdk_ec2.types.enable_ipam_organization_admin_account_result


def enable_ipam_organization_admin_account(
    options: OperationOptions,
    input: aws_sdk_ec2.types.enable_ipam_organization_admin_account_request.EnableIpamOrganizationAdminAccountRequest,
) -> tuple[
    aws_sdk_ec2.types.enable_ipam_organization_admin_account_result.EnableIpamOrganizationAdminAccountResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_enable_ipam_organization_admin_account(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.enable_ipam_organization_admin_account_request.EnableIpamOrganizationAdminAccountRequest,
) -> tuple[
    aws_sdk_ec2.types.enable_ipam_organization_admin_account_result.EnableIpamOrganizationAdminAccountResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
