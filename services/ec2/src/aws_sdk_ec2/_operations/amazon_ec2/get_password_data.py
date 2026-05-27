"""Generated from Smithy shape ``com.amazonaws.ec2#GetPasswordData``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_password_data_request
    import aws_sdk_ec2.types.get_password_data_result


def get_password_data(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_password_data_request.GetPasswordDataRequest,
) -> tuple[
    aws_sdk_ec2.types.get_password_data_result.GetPasswordDataResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_password_data(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_password_data_request.GetPasswordDataRequest,
) -> tuple[
    aws_sdk_ec2.types.get_password_data_result.GetPasswordDataResult, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
