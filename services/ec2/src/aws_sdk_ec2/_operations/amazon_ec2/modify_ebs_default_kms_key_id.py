"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyEbsDefaultKmsKeyId``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_ebs_default_kms_key_id_request
    import aws_sdk_ec2.types.modify_ebs_default_kms_key_id_result


def modify_ebs_default_kms_key_id(
    options: OperationOptions,
    input: aws_sdk_ec2.types.modify_ebs_default_kms_key_id_request.ModifyEbsDefaultKmsKeyIdRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_ebs_default_kms_key_id_result.ModifyEbsDefaultKmsKeyIdResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_modify_ebs_default_kms_key_id(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.modify_ebs_default_kms_key_id_request.ModifyEbsDefaultKmsKeyIdRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_ebs_default_kms_key_id_result.ModifyEbsDefaultKmsKeyIdResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
