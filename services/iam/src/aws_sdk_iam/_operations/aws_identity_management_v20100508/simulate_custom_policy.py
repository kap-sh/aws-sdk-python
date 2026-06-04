"""Generated from Smithy shape ``com.amazonaws.iam#SimulateCustomPolicy``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_iam._auth._signers
from aws_sdk_iam._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_iam.types.simulate_custom_policy_request
    import aws_sdk_iam.types.simulate_policy_response


def simulate_custom_policy(
    options: OperationOptions,
    input: aws_sdk_iam.types.simulate_custom_policy_request.SimulateCustomPolicyRequest,
) -> tuple[
    aws_sdk_iam.types.simulate_policy_response.SimulatePolicyResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_simulate_custom_policy(
    options: AsyncOperationOptions,
    input: aws_sdk_iam.types.simulate_custom_policy_request.SimulateCustomPolicyRequest,
) -> tuple[
    aws_sdk_iam.types.simulate_policy_response.SimulatePolicyResponse, zapros.Response
]:
    raise NotImplementedError("operation dispatch not yet generated")
