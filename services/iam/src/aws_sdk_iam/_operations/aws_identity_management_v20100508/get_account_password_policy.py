"""Generated from Smithy shape ``com.amazonaws.iam#GetAccountPasswordPolicy``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.get_account_password_policy_response


def get_account_password_policy(
    options: OperationOptions,
) -> tuple[
    aws_sdk_iam.types.get_account_password_policy_response.GetAccountPasswordPolicyResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_account_password_policy(
    options: AsyncOperationOptions,
) -> tuple[
    aws_sdk_iam.types.get_account_password_policy_response.GetAccountPasswordPolicyResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
