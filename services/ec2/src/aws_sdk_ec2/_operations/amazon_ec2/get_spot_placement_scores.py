"""Generated from Smithy shape ``com.amazonaws.ec2#GetSpotPlacementScores``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_spot_placement_scores_request
    import aws_sdk_ec2.types.get_spot_placement_scores_result


def get_spot_placement_scores(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_spot_placement_scores_request.GetSpotPlacementScoresRequest,
) -> tuple[
    aws_sdk_ec2.types.get_spot_placement_scores_result.GetSpotPlacementScoresResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_spot_placement_scores(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_spot_placement_scores_request.GetSpotPlacementScoresRequest,
) -> tuple[
    aws_sdk_ec2.types.get_spot_placement_scores_result.GetSpotPlacementScoresResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
