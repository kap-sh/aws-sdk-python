"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVerifiedAccessGroupPolicy``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_verified_access_group_policy_request
    import aws_sdk_ec2.types.modify_verified_access_group_policy_result


def modify_verified_access_group_policy(
    options: OperationOptions,
    input: aws_sdk_ec2.types.modify_verified_access_group_policy_request.ModifyVerifiedAccessGroupPolicyRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_verified_access_group_policy_result.ModifyVerifiedAccessGroupPolicyResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_modify_verified_access_group_policy(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.modify_verified_access_group_policy_request.ModifyVerifiedAccessGroupPolicyRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_verified_access_group_policy_result.ModifyVerifiedAccessGroupPolicyResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
