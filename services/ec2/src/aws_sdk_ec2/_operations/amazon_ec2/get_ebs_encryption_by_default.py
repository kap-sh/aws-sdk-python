"""Generated from Smithy shape ``com.amazonaws.ec2#GetEbsEncryptionByDefault``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_ebs_encryption_by_default_request
    import aws_sdk_ec2.types.get_ebs_encryption_by_default_result


def get_ebs_encryption_by_default(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_ebs_encryption_by_default_request.GetEbsEncryptionByDefaultRequest,
) -> tuple[
    aws_sdk_ec2.types.get_ebs_encryption_by_default_result.GetEbsEncryptionByDefaultResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_ebs_encryption_by_default(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_ebs_encryption_by_default_request.GetEbsEncryptionByDefaultRequest,
) -> tuple[
    aws_sdk_ec2.types.get_ebs_encryption_by_default_result.GetEbsEncryptionByDefaultResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
