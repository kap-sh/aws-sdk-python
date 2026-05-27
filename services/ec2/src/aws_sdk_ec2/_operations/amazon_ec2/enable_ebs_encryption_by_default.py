"""Generated from Smithy shape ``com.amazonaws.ec2#EnableEbsEncryptionByDefault``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.enable_ebs_encryption_by_default_request
    import aws_sdk_ec2.types.enable_ebs_encryption_by_default_result


def enable_ebs_encryption_by_default(
    options: OperationOptions,
    input: aws_sdk_ec2.types.enable_ebs_encryption_by_default_request.EnableEbsEncryptionByDefaultRequest,
) -> tuple[
    aws_sdk_ec2.types.enable_ebs_encryption_by_default_result.EnableEbsEncryptionByDefaultResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_enable_ebs_encryption_by_default(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.enable_ebs_encryption_by_default_request.EnableEbsEncryptionByDefaultRequest,
) -> tuple[
    aws_sdk_ec2.types.enable_ebs_encryption_by_default_result.EnableEbsEncryptionByDefaultResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
