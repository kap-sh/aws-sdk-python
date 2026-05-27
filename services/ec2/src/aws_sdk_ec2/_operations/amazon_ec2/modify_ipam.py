"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyIpam``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_ipam_request
    import aws_sdk_ec2.types.modify_ipam_result


def modify_ipam(
    options: OperationOptions,
    input: aws_sdk_ec2.types.modify_ipam_request.ModifyIpamRequest,
) -> tuple[aws_sdk_ec2.types.modify_ipam_result.ModifyIpamResult, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_modify_ipam(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.modify_ipam_request.ModifyIpamRequest,
) -> tuple[aws_sdk_ec2.types.modify_ipam_result.ModifyIpamResult, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
