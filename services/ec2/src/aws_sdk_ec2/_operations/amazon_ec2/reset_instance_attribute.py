"""Generated from Smithy shape ``com.amazonaws.ec2#ResetInstanceAttribute``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.reset_instance_attribute_request


def reset_instance_attribute(
    options: OperationOptions,
    input: aws_sdk_ec2.types.reset_instance_attribute_request.ResetInstanceAttributeRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_reset_instance_attribute(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.reset_instance_attribute_request.ResetInstanceAttributeRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
