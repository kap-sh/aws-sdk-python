"""Generated from Smithy shape ``com.amazonaws.ec2#DeleteVpcPeeringConnection``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.delete_vpc_peering_connection_request
    import aws_sdk_ec2.types.delete_vpc_peering_connection_result


def delete_vpc_peering_connection(
    options: OperationOptions,
    input: aws_sdk_ec2.types.delete_vpc_peering_connection_request.DeleteVpcPeeringConnectionRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_vpc_peering_connection_result.DeleteVpcPeeringConnectionResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_delete_vpc_peering_connection(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.delete_vpc_peering_connection_request.DeleteVpcPeeringConnectionRequest,
) -> tuple[
    aws_sdk_ec2.types.delete_vpc_peering_connection_result.DeleteVpcPeeringConnectionResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
