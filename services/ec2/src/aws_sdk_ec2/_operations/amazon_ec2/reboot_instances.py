"""Generated from Smithy shape ``com.amazonaws.ec2#RebootInstances``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.reboot_instances_request


def reboot_instances(
    options: OperationOptions,
    input: aws_sdk_ec2.types.reboot_instances_request.RebootInstancesRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_reboot_instances(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.reboot_instances_request.RebootInstancesRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
