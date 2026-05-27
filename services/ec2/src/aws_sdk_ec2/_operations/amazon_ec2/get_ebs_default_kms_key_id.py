"""Generated from Smithy shape ``com.amazonaws.ec2#GetEbsDefaultKmsKeyId``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_ebs_default_kms_key_id_request
    import aws_sdk_ec2.types.get_ebs_default_kms_key_id_result


def get_ebs_default_kms_key_id(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_ebs_default_kms_key_id_request.GetEbsDefaultKmsKeyIdRequest,
) -> tuple[
    aws_sdk_ec2.types.get_ebs_default_kms_key_id_result.GetEbsDefaultKmsKeyIdResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_ebs_default_kms_key_id(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_ebs_default_kms_key_id_request.GetEbsDefaultKmsKeyIdRequest,
) -> tuple[
    aws_sdk_ec2.types.get_ebs_default_kms_key_id_result.GetEbsDefaultKmsKeyIdResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
