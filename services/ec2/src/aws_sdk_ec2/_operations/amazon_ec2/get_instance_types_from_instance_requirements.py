"""Generated from Smithy shape ``com.amazonaws.ec2#GetInstanceTypesFromInstanceRequirements``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.get_instance_types_from_instance_requirements_request
    import aws_sdk_ec2.types.get_instance_types_from_instance_requirements_result


def get_instance_types_from_instance_requirements(
    options: OperationOptions,
    input: aws_sdk_ec2.types.get_instance_types_from_instance_requirements_request.GetInstanceTypesFromInstanceRequirementsRequest,
) -> tuple[
    aws_sdk_ec2.types.get_instance_types_from_instance_requirements_result.GetInstanceTypesFromInstanceRequirementsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_get_instance_types_from_instance_requirements(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.get_instance_types_from_instance_requirements_request.GetInstanceTypesFromInstanceRequirementsRequest,
) -> tuple[
    aws_sdk_ec2.types.get_instance_types_from_instance_requirements_result.GetInstanceTypesFromInstanceRequirementsResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
