"""Generated from Smithy shape ``com.amazonaws.iam#ListPolicyVersions``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.list_policy_versions_request
    import aws_sdk_iam.types.list_policy_versions_response


def list_policy_versions(
    options: OperationOptions,
    input: aws_sdk_iam.types.list_policy_versions_request.ListPolicyVersionsRequest,
) -> tuple[
    aws_sdk_iam.types.list_policy_versions_response.ListPolicyVersionsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_policy_versions(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.list_policy_versions_request.ListPolicyVersionsRequest,
) -> tuple[
    aws_sdk_iam.types.list_policy_versions_response.ListPolicyVersionsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
