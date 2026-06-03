"""Generated from Smithy shape ``com.amazonaws.kms#RotateKeyOnDemand``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_kms._auth._signers
from aws_sdk_kms._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_kms.types.rotate_key_on_demand_request
    import aws_sdk_kms.types.rotate_key_on_demand_response


def rotate_key_on_demand(
    options: OperationOptions,
    input: aws_sdk_kms.types.rotate_key_on_demand_request.RotateKeyOnDemandRequest,
) -> tuple[
    aws_sdk_kms.types.rotate_key_on_demand_response.RotateKeyOnDemandResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_rotate_key_on_demand(
    options: AsyncOperationOptions,
    input: aws_sdk_kms.types.rotate_key_on_demand_request.RotateKeyOnDemandRequest,
) -> tuple[
    aws_sdk_kms.types.rotate_key_on_demand_response.RotateKeyOnDemandResponse,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
