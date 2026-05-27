"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateIamInstanceProfile``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.associate_iam_instance_profile_request
    import aws_sdk_ec2.types.associate_iam_instance_profile_result


def associate_iam_instance_profile(
    options: OperationOptions,
    input: aws_sdk_ec2.types.associate_iam_instance_profile_request.AssociateIamInstanceProfileRequest,
) -> tuple[
    aws_sdk_ec2.types.associate_iam_instance_profile_result.AssociateIamInstanceProfileResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_associate_iam_instance_profile(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.associate_iam_instance_profile_request.AssociateIamInstanceProfileRequest,
) -> tuple[
    aws_sdk_ec2.types.associate_iam_instance_profile_result.AssociateIamInstanceProfileResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
