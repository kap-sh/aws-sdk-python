"""Generated from Smithy shape ``com.amazonaws.ec2#CreateMacSystemIntegrityProtectionModificationTask``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_mac_system_integrity_protection_modification_task_request
    import aws_sdk_ec2.types.create_mac_system_integrity_protection_modification_task_result


def create_mac_system_integrity_protection_modification_task(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_mac_system_integrity_protection_modification_task_request.CreateMacSystemIntegrityProtectionModificationTaskRequest,
) -> tuple[
    aws_sdk_ec2.types.create_mac_system_integrity_protection_modification_task_result.CreateMacSystemIntegrityProtectionModificationTaskResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_mac_system_integrity_protection_modification_task(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_mac_system_integrity_protection_modification_task_request.CreateMacSystemIntegrityProtectionModificationTaskRequest,
) -> tuple[
    aws_sdk_ec2.types.create_mac_system_integrity_protection_modification_task_result.CreateMacSystemIntegrityProtectionModificationTaskResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
