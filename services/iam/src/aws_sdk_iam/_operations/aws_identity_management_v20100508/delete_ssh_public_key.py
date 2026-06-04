"""Generated from Smithy shape ``com.amazonaws.iam#DeleteSSHPublicKey``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.delete_ssh_public_key_request


def delete_ssh_public_key(
    options: OperationOptions,
    input: aws_sdk_iam.types.delete_ssh_public_key_request.DeleteSSHPublicKeyRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_ssh_public_key(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.delete_ssh_public_key_request.DeleteSSHPublicKeyRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
