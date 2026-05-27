"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteVolume``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_volume_request


def delete_volume(
    options: OperationOptions,
    input: aws_sdk_ec2.types.delete_volume_request.DeleteVolumeRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_volume(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.delete_volume_request.DeleteVolumeRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
