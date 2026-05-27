"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVolume``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_volume_request
    import aws_sdk_ec2.types.volume


def create_volume(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_volume_request.CreateVolumeRequest,
) -> tuple[aws_sdk_ec2.types.volume.Volume, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_volume(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_volume_request.CreateVolumeRequest,
) -> tuple[aws_sdk_ec2.types.volume.Volume, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
