"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteSecondaryNetwork``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_secondary_network_request
    import aws_sdk_ec2.types.delete_secondary_network_result


def delete_secondary_network(
    options: OperationOptions,
    input: aws_sdk_ec2.types.delete_secondary_network_request.DeleteSecondaryNetworkRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_secondary_network_result.DeleteSecondaryNetworkResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_secondary_network(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.delete_secondary_network_request.DeleteSecondaryNetworkRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_secondary_network_result.DeleteSecondaryNetworkResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
