"""Generated from Smithy shape ``com.amazonaws.ec2#DescribeInstanceAttribute``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_instance_attribute_request
    import aws_sdk_ec2.types.instance_attribute


def describe_instance_attribute(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_instance_attribute_request.DescribeInstanceAttributeRequest,
) -> tuple[aws_sdk_ec2.types.instance_attribute.InstanceAttribute, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_instance_attribute(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_instance_attribute_request.DescribeInstanceAttributeRequest,
) -> tuple[aws_sdk_ec2.types.instance_attribute.InstanceAttribute, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
