"""Generated from Smithy shape ``com.amazonaws.iam#ListEntitiesForPolicy``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.list_entities_for_policy_request
    import aws_sdk_iam.types.list_entities_for_policy_response


def list_entities_for_policy(
    options: OperationOptions,
    input: aws_sdk_iam.types.list_entities_for_policy_request.ListEntitiesForPolicyRequest,
) -> tuple[
    aws_sdk_iam.types.list_entities_for_policy_response.ListEntitiesForPolicyResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_entities_for_policy(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.list_entities_for_policy_request.ListEntitiesForPolicyRequest,
) -> tuple[
    aws_sdk_iam.types.list_entities_for_policy_response.ListEntitiesForPolicyResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
