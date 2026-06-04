"""Generated from Smithy shape ``com.amazonaws.iam#ListPolicies``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.list_policies_request
    import aws_sdk_iam.types.list_policies_response


def list_policies(
    options: OperationOptions,
    input: aws_sdk_iam.types.list_policies_request.ListPoliciesRequest,
) -> tuple[
    aws_sdk_iam.types.list_policies_response.ListPoliciesResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_policies(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.list_policies_request.ListPoliciesRequest,
) -> tuple[
    aws_sdk_iam.types.list_policies_response.ListPoliciesResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
