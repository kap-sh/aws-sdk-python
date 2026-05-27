"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyInstancePlacement``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_instance_placement_request
    import aws_sdk_ec2.types.modify_instance_placement_result


def modify_instance_placement(
    options: OperationOptions,
    input: aws_sdk_ec2.types.modify_instance_placement_request.ModifyInstancePlacementRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_instance_placement_result.ModifyInstancePlacementResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_modify_instance_placement(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.modify_instance_placement_request.ModifyInstancePlacementRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_instance_placement_result.ModifyInstancePlacementResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
