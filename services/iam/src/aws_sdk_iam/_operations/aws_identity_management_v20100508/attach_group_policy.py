"""Generated from Smithy shape ``com.amazonaws.iam#AttachGroupPolicy``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.attach_group_policy_request


def attach_group_policy(
    options: OperationOptions,
    input: aws_sdk_iam.types.attach_group_policy_request.AttachGroupPolicyRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_attach_group_policy(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.attach_group_policy_request.AttachGroupPolicyRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
