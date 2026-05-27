"""Generated from Smithy shape ``com.amazonaws.ec2#PurchaseCapacityBlockExtension``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.purchase_capacity_block_extension_request
    import aws_sdk_ec2.types.purchase_capacity_block_extension_result


def purchase_capacity_block_extension(
    options: OperationOptions,
    input: aws_sdk_ec2.types.purchase_capacity_block_extension_request.PurchaseCapacityBlockExtensionRequest,
) -> tuple[
    aws_sdk_ec2.types.purchase_capacity_block_extension_result.PurchaseCapacityBlockExtensionResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_purchase_capacity_block_extension(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.purchase_capacity_block_extension_request.PurchaseCapacityBlockExtensionRequest,
) -> tuple[
    aws_sdk_ec2.types.purchase_capacity_block_extension_result.PurchaseCapacityBlockExtensionResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
