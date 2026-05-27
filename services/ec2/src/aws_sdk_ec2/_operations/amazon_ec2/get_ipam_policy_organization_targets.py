"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamPolicyOrganizationTargets``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_ipam_policy_organization_targets_request
    import aws_sdk_ec2.types.get_ipam_policy_organization_targets_result


def get_ipam_policy_organization_targets(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_ipam_policy_organization_targets_request.GetIpamPolicyOrganizationTargetsRequest,
) -> tuple[
    aws_sdk_ec2.types.get_ipam_policy_organization_targets_result.GetIpamPolicyOrganizationTargetsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_ipam_policy_organization_targets(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_ipam_policy_organization_targets_request.GetIpamPolicyOrganizationTargetsRequest,
) -> tuple[
    aws_sdk_ec2.types.get_ipam_policy_organization_targets_result.GetIpamPolicyOrganizationTargetsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
