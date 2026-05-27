"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamPolicyAllocationRules``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_ipam_policy_allocation_rules_request
    import aws_sdk_ec2.types.get_ipam_policy_allocation_rules_result


def get_ipam_policy_allocation_rules(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_ipam_policy_allocation_rules_request.GetIpamPolicyAllocationRulesRequest,
) -> tuple[
    aws_sdk_ec2.types.get_ipam_policy_allocation_rules_result.GetIpamPolicyAllocationRulesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_ipam_policy_allocation_rules(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_ipam_policy_allocation_rules_request.GetIpamPolicyAllocationRulesRequest,
) -> tuple[
    aws_sdk_ec2.types.get_ipam_policy_allocation_rules_result.GetIpamPolicyAllocationRulesResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
