"""Generated from Smithy shape ``com.amazonaws.ec2#CreateIpamPolicy``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_ipam_policy_request
    import aws_sdk_ec2.types.create_ipam_policy_result


def create_ipam_policy(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_ipam_policy_request.CreateIpamPolicyRequest,
) -> tuple[
    aws_sdk_ec2.types.create_ipam_policy_result.CreateIpamPolicyResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_ipam_policy(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_ipam_policy_request.CreateIpamPolicyRequest,
) -> tuple[
    aws_sdk_ec2.types.create_ipam_policy_result.CreateIpamPolicyResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
