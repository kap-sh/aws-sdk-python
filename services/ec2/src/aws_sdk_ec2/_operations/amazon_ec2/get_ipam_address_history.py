"""Generated from Smithy shape ``com.amazonaws.ec2#GetIpamAddressHistory``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_ipam_address_history_request
    import aws_sdk_ec2.types.get_ipam_address_history_result


def get_ipam_address_history(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_ipam_address_history_request.GetIpamAddressHistoryRequest,
) -> tuple[
    aws_sdk_ec2.types.get_ipam_address_history_result.GetIpamAddressHistoryResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_ipam_address_history(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_ipam_address_history_request.GetIpamAddressHistoryRequest,
) -> tuple[
    aws_sdk_ec2.types.get_ipam_address_history_result.GetIpamAddressHistoryResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
