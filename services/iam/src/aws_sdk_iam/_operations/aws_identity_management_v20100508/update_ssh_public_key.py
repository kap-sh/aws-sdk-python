"""Generated from Smithy shape ``com.amazonaws.iam#UpdateSSHPublicKey``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.update_ssh_public_key_request


def update_ssh_public_key(
    options: OperationOptions,
    input: aws_sdk_iam.types.update_ssh_public_key_request.UpdateSSHPublicKeyRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_update_ssh_public_key(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.update_ssh_public_key_request.UpdateSSHPublicKeyRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
