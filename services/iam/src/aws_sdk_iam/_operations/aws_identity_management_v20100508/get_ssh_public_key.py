"""Generated from Smithy shape ``com.amazonaws.iam#GetSSHPublicKey``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.get_ssh_public_key_request
    import aws_sdk_iam.types.get_ssh_public_key_response


def get_ssh_public_key(
    options: OperationOptions,
    input: aws_sdk_iam.types.get_ssh_public_key_request.GetSSHPublicKeyRequest,
) -> tuple[
    aws_sdk_iam.types.get_ssh_public_key_response.GetSSHPublicKeyResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_ssh_public_key(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.get_ssh_public_key_request.GetSSHPublicKeyRequest,
) -> tuple[
    aws_sdk_iam.types.get_ssh_public_key_response.GetSSHPublicKeyResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
