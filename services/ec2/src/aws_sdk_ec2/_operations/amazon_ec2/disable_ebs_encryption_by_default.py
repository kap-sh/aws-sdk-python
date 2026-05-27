"""Generated from Smithy shape ``com.amazonaws.ec2#DisableEbsEncryptionByDefault``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disable_ebs_encryption_by_default_request
    import aws_sdk_ec2.types.disable_ebs_encryption_by_default_result


def disable_ebs_encryption_by_default(
    options: OperationOptions,
    input: aws_sdk_ec2.types.disable_ebs_encryption_by_default_request.DisableEbsEncryptionByDefaultRequest,
) -> tuple[
    aws_sdk_ec2.types.disable_ebs_encryption_by_default_result.DisableEbsEncryptionByDefaultResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_disable_ebs_encryption_by_default(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.disable_ebs_encryption_by_default_request.DisableEbsEncryptionByDefaultRequest,
) -> tuple[
    aws_sdk_ec2.types.disable_ebs_encryption_by_default_result.DisableEbsEncryptionByDefaultResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
