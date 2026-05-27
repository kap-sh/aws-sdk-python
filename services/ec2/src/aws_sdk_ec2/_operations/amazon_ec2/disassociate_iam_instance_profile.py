"""Generated from Smithy shape ``com.amazonaws.ec2#DisassociateIamInstanceProfile``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.disassociate_iam_instance_profile_request
    import aws_sdk_ec2.types.disassociate_iam_instance_profile_result


def disassociate_iam_instance_profile(
    options: OperationOptions,
    input: aws_sdk_ec2.types.disassociate_iam_instance_profile_request.DisassociateIamInstanceProfileRequest,
) -> tuple[
    aws_sdk_ec2.types.disassociate_iam_instance_profile_result.DisassociateIamInstanceProfileResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_disassociate_iam_instance_profile(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.disassociate_iam_instance_profile_request.DisassociateIamInstanceProfileRequest,
) -> tuple[
    aws_sdk_ec2.types.disassociate_iam_instance_profile_result.DisassociateIamInstanceProfileResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
