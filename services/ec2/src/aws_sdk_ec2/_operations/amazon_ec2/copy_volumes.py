"""Generated from Smithy shape ``com.amazonaws.ec2#CopyVolumes``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.copy_volumes_request
    import aws_sdk_ec2.types.copy_volumes_result


def copy_volumes(
    options: OperationOptions,
    input: aws_sdk_ec2.types.copy_volumes_request.CopyVolumesRequest,
) -> tuple[aws_sdk_ec2.types.copy_volumes_result.CopyVolumesResult, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_copy_volumes(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.copy_volumes_request.CopyVolumesRequest,
) -> tuple[aws_sdk_ec2.types.copy_volumes_result.CopyVolumesResult, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
