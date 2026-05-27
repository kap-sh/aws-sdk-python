"""Generated from Smithy shape ``com.amazonaws.ec2#ImportInstance``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.import_instance_request
    import aws_sdk_ec2.types.import_instance_result


def import_instance(
    options: OperationOptions,
    input: aws_sdk_ec2.types.import_instance_request.ImportInstanceRequest,
) -> tuple[
    aws_sdk_ec2.types.import_instance_result.ImportInstanceResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_import_instance(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.import_instance_request.ImportInstanceRequest,
) -> tuple[
    aws_sdk_ec2.types.import_instance_result.ImportInstanceResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
