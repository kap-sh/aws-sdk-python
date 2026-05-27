"""Generated from Smithy shape ``com.amazonaws.ec2#CreateCapacityManagerDataExport``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_capacity_manager_data_export_request
    import aws_sdk_ec2.types.create_capacity_manager_data_export_result


def create_capacity_manager_data_export(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_capacity_manager_data_export_request.CreateCapacityManagerDataExportRequest,
) -> tuple[
    aws_sdk_ec2.types.create_capacity_manager_data_export_result.CreateCapacityManagerDataExportResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_capacity_manager_data_export(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_capacity_manager_data_export_request.CreateCapacityManagerDataExportRequest,
) -> tuple[
    aws_sdk_ec2.types.create_capacity_manager_data_export_result.CreateCapacityManagerDataExportResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
