"""Generated from Smithy shape ``com.amazonaws.ec2#CreateKeyPair``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_key_pair_request
    import aws_sdk_ec2.types.key_pair


def create_key_pair(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_key_pair_request.CreateKeyPairRequest,
) -> tuple[aws_sdk_ec2.types.key_pair.KeyPair, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_key_pair(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_key_pair_request.CreateKeyPairRequest,
) -> tuple[aws_sdk_ec2.types.key_pair.KeyPair, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
