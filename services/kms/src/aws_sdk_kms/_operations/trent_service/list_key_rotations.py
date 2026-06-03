"""Generated from Smithy shape ``com.amazonaws.kms#ListKeyRotations``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_kms._auth._signers
from aws_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_kms.types.list_key_rotations_request
    import aws_sdk_kms.types.list_key_rotations_response


def list_key_rotations(
    options: OperationOptions,
    input: aws_sdk_kms.types.list_key_rotations_request.ListKeyRotationsRequest,
) -> tuple[
    aws_sdk_kms.types.list_key_rotations_response.ListKeyRotationsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_list_key_rotations(
    options: AsyncOperationOptions,
    input: aws_sdk_kms.types.list_key_rotations_request.ListKeyRotationsRequest,
) -> tuple[
    aws_sdk_kms.types.list_key_rotations_response.ListKeyRotationsResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
