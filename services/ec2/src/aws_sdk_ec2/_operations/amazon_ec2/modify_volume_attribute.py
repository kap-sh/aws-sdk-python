"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVolumeAttribute``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_volume_attribute_request


def modify_volume_attribute(
    options: OperationOptions,
    input: aws_sdk_ec2.types.modify_volume_attribute_request.ModifyVolumeAttributeRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_modify_volume_attribute(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.modify_volume_attribute_request.ModifyVolumeAttributeRequest,
) -> tuple[None, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
