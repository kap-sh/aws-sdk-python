"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVerifiedAccessEndpointPolicy``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_verified_access_endpoint_policy_request
    import aws_sdk_ec2.types.modify_verified_access_endpoint_policy_result


def modify_verified_access_endpoint_policy(
    options: OperationOptions,
    input: aws_sdk_ec2.types.modify_verified_access_endpoint_policy_request.ModifyVerifiedAccessEndpointPolicyRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_verified_access_endpoint_policy_result.ModifyVerifiedAccessEndpointPolicyResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_modify_verified_access_endpoint_policy(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.modify_verified_access_endpoint_policy_request.ModifyVerifiedAccessEndpointPolicyRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_verified_access_endpoint_policy_result.ModifyVerifiedAccessEndpointPolicyResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
