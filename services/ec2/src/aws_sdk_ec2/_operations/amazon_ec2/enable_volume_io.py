"""Generated from Smithy shape ``com.amazonaws.ec2#EnableVolumeIO``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.enable_volume_io_request


def enable_volume_io(
    options: OperationOptions,
    input: aws_sdk_ec2.types.enable_volume_io_request.EnableVolumeIORequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_enable_volume_io(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.enable_volume_io_request.EnableVolumeIORequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
