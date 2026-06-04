"""Generated from Smithy shape ``com.amazonaws.iam#ListSSHPublicKeys``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.list_ssh_public_keys_request
    import aws_sdk_iam.types.list_ssh_public_keys_response


def list_ssh_public_keys(
    options: OperationOptions,
    input: aws_sdk_iam.types.list_ssh_public_keys_request.ListSSHPublicKeysRequest,
) -> tuple[
    aws_sdk_iam.types.list_ssh_public_keys_response.ListSSHPublicKeysResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_ssh_public_keys(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.list_ssh_public_keys_request.ListSSHPublicKeysRequest,
) -> tuple[
    aws_sdk_iam.types.list_ssh_public_keys_response.ListSSHPublicKeysResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
