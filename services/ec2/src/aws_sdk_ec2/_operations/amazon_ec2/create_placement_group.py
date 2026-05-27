"""Generated from Smithy shape ``com.amazonaws.ec2#CreatePlacementGroup``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.create_placement_group_request
    import aws_sdk_ec2.types.create_placement_group_result


def create_placement_group(
    options: OperationOptions,
    input: aws_sdk_ec2.types.create_placement_group_request.CreatePlacementGroupRequest,
) -> tuple[
    aws_sdk_ec2.types.create_placement_group_result.CreatePlacementGroupResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_create_placement_group(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.create_placement_group_request.CreatePlacementGroupRequest,
) -> tuple[
    aws_sdk_ec2.types.create_placement_group_result.CreatePlacementGroupResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
