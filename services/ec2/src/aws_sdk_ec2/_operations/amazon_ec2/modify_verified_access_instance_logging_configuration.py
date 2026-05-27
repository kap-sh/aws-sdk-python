"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVerifiedAccessInstanceLoggingConfiguration``."""

from __future__ import annotations
from typing import TYPE_CHECKING
import zapros
import aws_sdk_ec2._auth._signers
from aws_sdk_ec2._services._pipeline import AsyncOperationOptions, OperationOptions

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_verified_access_instance_logging_configuration_request
    import aws_sdk_ec2.types.modify_verified_access_instance_logging_configuration_result


def modify_verified_access_instance_logging_configuration(
    options: OperationOptions,
    input: aws_sdk_ec2.types.modify_verified_access_instance_logging_configuration_request.ModifyVerifiedAccessInstanceLoggingConfigurationRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_verified_access_instance_logging_configuration_result.ModifyVerifiedAccessInstanceLoggingConfigurationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")


async def async_modify_verified_access_instance_logging_configuration(
    options: AsyncOperationOptions,
    input: aws_sdk_ec2.types.modify_verified_access_instance_logging_configuration_request.ModifyVerifiedAccessInstanceLoggingConfigurationRequest,
) -> tuple[
    aws_sdk_ec2.types.modify_verified_access_instance_logging_configuration_result.ModifyVerifiedAccessInstanceLoggingConfigurationResult,
    zapros.Response,
]:
    raise NotImplementedError("operation dispatch not yet generated")
