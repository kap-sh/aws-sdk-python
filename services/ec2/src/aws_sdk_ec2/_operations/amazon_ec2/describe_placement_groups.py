"""Generated from Smithy shape ``com.amazonaws.ec2#DescribePlacementGroups``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.describe_placement_groups_request
    import aws_sdk_ec2.types.describe_placement_groups_result


def describe_placement_groups(
    options: OperationOptions,
    input: aws_sdk_ec2.types.describe_placement_groups_request.DescribePlacementGroupsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_placement_groups_result.DescribePlacementGroupsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_describe_placement_groups(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.describe_placement_groups_request.DescribePlacementGroupsRequest,
) -> tuple[
    aws_sdk_ec2.types.describe_placement_groups_result.DescribePlacementGroupsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
