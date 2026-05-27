"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyHosts``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_hosts_request
    import aws_sdk_ec2.types.modify_hosts_result


def modify_hosts(
    options: OperationOptions,
    input: aws_sdk_ec2.types.modify_hosts_request.ModifyHostsRequest,
) -> tuple[aws_sdk_ec2.types.modify_hosts_result.ModifyHostsResult, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_modify_hosts(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.modify_hosts_request.ModifyHostsRequest,
) -> tuple[aws_sdk_ec2.types.modify_hosts_result.ModifyHostsResult, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
