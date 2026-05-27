"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVpcPeeringConnection``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_vpc_peering_connection_request
    import aws_sdk_ec2.types.create_vpc_peering_connection_result


def create_vpc_peering_connection(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_vpc_peering_connection_request.CreateVpcPeeringConnectionRequest,
) -> tuple[
    aws_sdk_ec2.types.create_vpc_peering_connection_result.CreateVpcPeeringConnectionResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_vpc_peering_connection(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_vpc_peering_connection_request.CreateVpcPeeringConnectionRequest,
) -> tuple[
    aws_sdk_ec2.types.create_vpc_peering_connection_result.CreateVpcPeeringConnectionResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
