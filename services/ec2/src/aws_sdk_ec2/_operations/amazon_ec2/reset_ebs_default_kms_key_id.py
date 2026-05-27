"""Generated from Smithy shape ``com.amazonaws.ec2#ResetEbsDefaultKmsKeyId``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.reset_ebs_default_kms_key_id_request
    import aws_sdk_ec2.types.reset_ebs_default_kms_key_id_result


def reset_ebs_default_kms_key_id(
    options: OperationOptions,
    input: aws_sdk_ec2.types.reset_ebs_default_kms_key_id_request.ResetEbsDefaultKmsKeyIdRequest,
) -> tuple[
    aws_sdk_ec2.types.reset_ebs_default_kms_key_id_result.ResetEbsDefaultKmsKeyIdResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_reset_ebs_default_kms_key_id(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.reset_ebs_default_kms_key_id_request.ResetEbsDefaultKmsKeyIdRequest,
) -> tuple[
    aws_sdk_ec2.types.reset_ebs_default_kms_key_id_result.ResetEbsDefaultKmsKeyIdResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
