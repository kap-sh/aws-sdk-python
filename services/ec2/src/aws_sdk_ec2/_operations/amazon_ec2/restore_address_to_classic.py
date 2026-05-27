"""Generated from Smithy shape ``com.amazonaws.ec2#RestoreAddressToClassic``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.restore_address_to_classic_request
    import aws_sdk_ec2.types.restore_address_to_classic_result


def restore_address_to_classic(
    options: OperationOptions,
    input: aws_sdk_ec2.types.restore_address_to_classic_request.RestoreAddressToClassicRequest,
) -> tuple[
    aws_sdk_ec2.types.restore_address_to_classic_result.RestoreAddressToClassicResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_restore_address_to_classic(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.restore_address_to_classic_request.RestoreAddressToClassicRequest,
) -> tuple[
    aws_sdk_ec2.types.restore_address_to_classic_result.RestoreAddressToClassicResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
