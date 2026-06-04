"""Generated from Smithy shape ``com.amazonaws.iam#ListGroupPolicies``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.list_group_policies_request
    import aws_sdk_iam.types.list_group_policies_response


def list_group_policies(
    options: OperationOptions,
    input: aws_sdk_iam.types.list_group_policies_request.ListGroupPoliciesRequest,
) -> tuple[
    aws_sdk_iam.types.list_group_policies_response.ListGroupPoliciesResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_group_policies(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.list_group_policies_request.ListGroupPoliciesRequest,
) -> tuple[
    aws_sdk_iam.types.list_group_policies_response.ListGroupPoliciesResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
