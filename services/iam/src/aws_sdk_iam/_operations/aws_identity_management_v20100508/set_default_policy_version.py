"""Generated from Smithy shape ``com.amazonaws.iam#SetDefaultPolicyVersion``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.set_default_policy_version_request


def set_default_policy_version(
    options: OperationOptions,
    input: aws_sdk_iam.types.set_default_policy_version_request.SetDefaultPolicyVersionRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_set_default_policy_version(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.set_default_policy_version_request.SetDefaultPolicyVersionRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
