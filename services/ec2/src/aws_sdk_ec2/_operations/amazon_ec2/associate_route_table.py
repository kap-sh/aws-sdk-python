"""Generated from Smithy shape ``com.amazonaws.ec2#AssociateRouteTable``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.associate_route_table_request
    import aws_sdk_ec2.types.associate_route_table_result


def associate_route_table(
    options: OperationOptions,
    input: aws_sdk_ec2.types.associate_route_table_request.AssociateRouteTableRequest,
) -> tuple[
    aws_sdk_ec2.types.associate_route_table_result.AssociateRouteTableResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_associate_route_table(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.associate_route_table_request.AssociateRouteTableRequest,
) -> tuple[
    aws_sdk_ec2.types.associate_route_table_result.AssociateRouteTableResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
