"""Generated from Smithy shape ``com.amazonaws.ec2#ReleaseHosts``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.release_hosts_request
    import aws_sdk_ec2.types.release_hosts_result


def release_hosts(
    options: OperationOptions,
    input: aws_sdk_ec2.types.release_hosts_request.ReleaseHostsRequest,
) -> tuple[aws_sdk_ec2.types.release_hosts_result.ReleaseHostsResult, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_release_hosts(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.release_hosts_request.ReleaseHostsRequest,
) -> tuple[aws_sdk_ec2.types.release_hosts_result.ReleaseHostsResult, zapros.Response]:
    raise NotImplementedError("operation dispatch not yet generated")
