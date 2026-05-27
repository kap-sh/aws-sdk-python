"""Generated from Smithy shape ``com.amazonaws.ec2#DisableIpamOrganizationAdminAccount``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disable_ipam_organization_admin_account_request
    import aws_sdk_ec2.types.disable_ipam_organization_admin_account_result


def disable_ipam_organization_admin_account(
    options: OperationOptions,
    input: aws_sdk_ec2.types.disable_ipam_organization_admin_account_request.DisableIpamOrganizationAdminAccountRequest,
) -> tuple[
    aws_sdk_ec2.types.disable_ipam_organization_admin_account_result.DisableIpamOrganizationAdminAccountResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_disable_ipam_organization_admin_account(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.disable_ipam_organization_admin_account_request.DisableIpamOrganizationAdminAccountRequest,
) -> tuple[
    aws_sdk_ec2.types.disable_ipam_organization_admin_account_result.DisableIpamOrganizationAdminAccountResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
