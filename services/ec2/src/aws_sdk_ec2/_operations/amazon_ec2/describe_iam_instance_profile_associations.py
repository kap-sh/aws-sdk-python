"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeIamInstanceProfileAssociations``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_iam_instance_profile_associations_request
    import aws_sdk_ec2.types.describe_iam_instance_profile_associations_result


def describe_iam_instance_profile_associations(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_iam_instance_profile_associations_request.DescribeIamInstanceProfileAssociationsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_iam_instance_profile_associations_result.DescribeIamInstanceProfileAssociationsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_iam_instance_profile_associations(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_iam_instance_profile_associations_request.DescribeIamInstanceProfileAssociationsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_iam_instance_profile_associations_result.DescribeIamInstanceProfileAssociationsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
