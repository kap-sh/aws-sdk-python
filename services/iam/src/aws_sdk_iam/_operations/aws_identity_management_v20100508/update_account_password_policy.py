"""Generated from Smithy shape ``com.amazonaws.iam#UpdateAccountPasswordPolicy``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.update_account_password_policy_request


def update_account_password_policy(
    options: OperationOptions,
    input: aws_sdk_iam.types.update_account_password_policy_request.UpdateAccountPasswordPolicyRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_update_account_password_policy(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.update_account_password_policy_request.UpdateAccountPasswordPolicyRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
