"""Generated from Smithy shape ``com.amazonaws.iam#UploadSSHPublicKey``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.upload_ssh_public_key_request
    import aws_sdk_iam.types.upload_ssh_public_key_response


def upload_ssh_public_key(
    options: OperationOptions,
    input: aws_sdk_iam.types.upload_ssh_public_key_request.UploadSSHPublicKeyRequest,
) -> tuple[
    aws_sdk_iam.types.upload_ssh_public_key_response.UploadSSHPublicKeyResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_upload_ssh_public_key(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.upload_ssh_public_key_request.UploadSSHPublicKeyRequest,
) -> tuple[
    aws_sdk_iam.types.upload_ssh_public_key_response.UploadSSHPublicKeyResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
