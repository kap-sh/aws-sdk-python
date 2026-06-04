"""Generated from Smithy shape ``com.amazonaws.iam#GetContextKeysForCustomPolicy``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.get_context_keys_for_custom_policy_request
    import aws_sdk_iam.types.get_context_keys_for_policy_response


def get_context_keys_for_custom_policy(
    options: OperationOptions,
    input: aws_sdk_iam.types.get_context_keys_for_custom_policy_request.GetContextKeysForCustomPolicyRequest,
) -> tuple[
    aws_sdk_iam.types.get_context_keys_for_policy_response.GetContextKeysForPolicyResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_context_keys_for_custom_policy(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.get_context_keys_for_custom_policy_request.GetContextKeysForCustomPolicyRequest,
) -> tuple[
    aws_sdk_iam.types.get_context_keys_for_policy_response.GetContextKeysForPolicyResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
