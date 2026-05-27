"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceCreditSpecifications``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_instance_credit_specifications_request
    import aws_sdk_ec2.types.describe_instance_credit_specifications_result


def describe_instance_credit_specifications(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_instance_credit_specifications_request.DescribeInstanceCreditSpecificationsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_instance_credit_specifications_result.DescribeInstanceCreditSpecificationsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_instance_credit_specifications(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_instance_credit_specifications_request.DescribeInstanceCreditSpecificationsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_instance_credit_specifications_result.DescribeInstanceCreditSpecificationsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
