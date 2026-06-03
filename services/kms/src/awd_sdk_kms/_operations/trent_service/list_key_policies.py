"""Generated from Smithy shape ``com.amazonaws.kms#ListKeyPolicies``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import awd_sdk_kms._auth._signers
from awd_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import awd_sdk_kms.types.list_key_policies_request
    import awd_sdk_kms.types.list_key_policies_response


def list_key_policies(
    options: OperationOptions,
    input: awd_sdk_kms.types.list_key_policies_request.ListKeyPoliciesRequest,
) -> tuple[
    awd_sdk_kms.types.list_key_policies_response.ListKeyPoliciesResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_key_policies(
    options: AsyncOperationOptions,
    input: awd_sdk_kms.types.list_key_policies_request.ListKeyPoliciesRequest,
) -> tuple[
    awd_sdk_kms.types.list_key_policies_response.ListKeyPoliciesResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
