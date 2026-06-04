"""Generated from Smithy shape ``com.amazonaws.iam#UntagInstanceProfile``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.untag_instance_profile_request


def untag_instance_profile(
    options: OperationOptions,
    input: aws_sdk_iam.types.untag_instance_profile_request.UntagInstanceProfileRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_untag_instance_profile(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.untag_instance_profile_request.UntagInstanceProfileRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
