"""Generated from Smithy shape ``com.amazonaws.ec2#GetInstanceUefiData``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_instance_uefi_data_request
    import aws_sdk_ec2.types.get_instance_uefi_data_result


def get_instance_uefi_data(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_instance_uefi_data_request.GetInstanceUefiDataRequest,
) -> tuple[
    aws_sdk_ec2.types.get_instance_uefi_data_result.GetInstanceUefiDataResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_instance_uefi_data(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_instance_uefi_data_request.GetInstanceUefiDataRequest,
) -> tuple[
    aws_sdk_ec2.types.get_instance_uefi_data_result.GetInstanceUefiDataResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
